# Import Beam Libraries

import apache_beam as beam
from apache_beam.runners import DataflowRunner
from apache_beam.options.pipeline_options import PipelineOptions
import apache_beam.transforms.window as window
from apache_beam.metrics import Metrics

# Dataflow ML
from apache_beam.ml.inference.base import ModelHandler
from apache_beam.ml.inference.base import RunInference

# Import GCP Libraries
from google.cloud.vision_v1.types import Feature
from google.cloud import vision

# Import Common Libraries
import argparse
import requests
import logging
import json
import re
import io

beam.options.pipeline_options.PipelineOptions.allow_non_parallel_instruction_output = True
DataflowRunner.__test__ = False


""" Helpful functions """
def ParsePubSubMessage(message):

    # Decode message
    pubsub_message = message.decode('utf-8')
    # Convert string decoded in JSON format
    json_msg = json.loads(pubsub_message)
    
    logging.info("New message from Publisher: %s", json_msg)

    return json_msg

def getVehicleImage(item,api_url):

    import requests
    import io

    img_service = requests.get(api_url)
    img_url = json.loads(img_service.content.decode('utf-8'))[img_url]

    # Read the image (using io.BytesIO) from the Google Cloud Storage URL obtained in the previous step.
    img_response = requests.get(img_url)
    img = io.BytesIO(img_response.content).read()

    # Append image_url to the payload
    item['image_url'] = img_url

    return item, img 


class CloudVisionModelHandler(ModelHandler):

    def load_model(self):
        
        """Initiate the Google Vision API client."""

        from google.cloud import vision
        
        client = vision.ImageAnnotatorClient()
        return client
    
    # def run_inference(self, batch, model, inference):

    #     from google.cloud import vision
    #     from google.cloud.vision_v1.types import Feature

    #     feature = Feature()
    #     feature.type_ = Feature.Type.TEXT_DETECTION

    #     images = [vision.Image(content=image_bytes) for (item, image_bytes) in batch]
    #     item_list = [item for (item, image_bytes) in batch]

    #     image_requests = [vision.AnnotateImageRequest(image=image, features=[feature]) for image in images]
    #     batch_image_request = vision.BatchAnnotateImagesRequest(requests=image_requests)

    #     model_responses = model.batch_annotate_images(request=batch_image_request).responses

    #     # Deal with the model's response to extract the text we need
    #     # ToDo: Complete this section
        
    #     yield output_dict, response

class OutputFormatDoFn(beam.DoFn):

    def process(self, element):

        output_dict, texts = element

        if len(texts) > 0 :

            # Set the pattern to recognize the license plate among the texts the model might find.
            output_dict['license_plate'] = texts[0] if len(texts) > 0 else "ERROR READING"
            
            yield output_dict

        else:

            output_dict['license_plate'] = "no texts found"
            yield output_dict
        

# DoFn

class getVehicleDoFn(beam.DoFn):

    def process(self, element):

        yield element['vehicle_id'], element
 

class avgSpeedDoFn(beam.DoFn):

    def __init__(self,radar_id):

        self.countFinedVehicles = Metrics.counter('main', 'Count of fined vehicles.')
        self.countNonFinedVehicles = Metrics.counter('main', 'Count of non-fined vehicles.')
        self.radar_id = radar_id

    def process(self, element):

        import apache_beam as beam
        
        key, payload = element

        speed = 0
        n = 0
        for car in payload:
            speed += car['speed']
            n += 1

        avg_speed = speed / n

        print(avg_speed)

        output_dict = {
            "radar_id": self.radar_id,
            "vehicle_id": key,
            "avg_speed": avg_speed,
            "coordinates": payload[-1]['location']
        }

        # Create two distinct PCollections, one for fined vehicles and another for those 
        # that have not been fined, so we can process the data differently.

        if avg_speed > 40:

            output_dict['is_Ticketed'] = True

            yield beam.pvalue.TaggedOutput("fined_vehicles", output_dict)
        
        else:

            output_dict['is_Ticketed'] = False
            output_dict['license_plate'] = None

            yield beam.pvalue.TaggedOutput("non_fined_vehicles", output_dict)


""" Dataflow Process """

def run():

    """ Input Arguments"""
    parser = argparse.ArgumentParser(description=('Arguments for the Dataflow Streaming Pipeline.'))

    parser.add_argument(
                '--project_id',
                required=True,
                help='GCP cloud project name.')
    
    parser.add_argument(
                '--input_subscription',
                required=True,
                help='PubSub subscription from which we will read data from the generator.')
    
    parser.add_argument(
                '--output_topic',
                required=True,
                help='PubSub Topic which will be the sink for our data.')

    parser.add_argument(
                '--radar_id',
                required=True,
                help="Radar ID corresponding to the student's name.")

    parser.add_argument(
                '--cars_api',
                required=True,
                help="API for retrieving vehicle images.")

    args, pipeline_opts = parser.parse_known_args()

    
    """ Apache Beam Pipeline """
    
    # Pipeline Options
    options = PipelineOptions(pipeline_opts,
        save_main_session=True, streaming=True, project=args.project_id)

    # Pipeline

    with beam.Pipeline(argv=pipeline_opts,options=options) as p:

        """ Part 01: Read data from PubSub. """

        data = (
            p
                | "Read From PubSub" >> beam.io.ReadFromPubSub(subscription=f'projects/{args.project_id}/subscriptions/{args.input_subscription}')
                | "Parse JSON messages" >> beam.ParDo(ParsePubSubMessage)
        )

        """ Part 02: Get the aggregated data of the vehicle within the section. """

        processed_data = (
            
            data 
                | "Extract vehicle id data" >> beam.ParDo(getVehicleDoFn())
                | "User-window based on each vehicle" >> beam.WindowInto(window.Sessions(11),timestamp_combiner=window.TimestampCombiner.OUTPUT_AT_EOW)
                | "Group by ID" >> beam.GroupByKey()
                | "Avg Speed" >> beam.ParDo(avgSpeedDoFn(radar_id=args.radar_id)).with_outputs('fined_vehicles', 'non_fined_vehicles')
        
        )

        (
            processed_data.fined_vehicles
                | "Capture Vehicle image" >> beam.Map(getVehicleImage, api_url=args.cars_api)
                | "Model Inference" >> RunInference(model_handler=CloudVisionModelHandler())
                | "Output Format" >> beam.ParDo(OutputFormatDoFn())
                | "Write fined_vehicles to BigQuery" >> beam.io.WriteToBigQuery(
                    table = f'{args.project_id}:coches.multados',
                    schema = 'radar_id:STRING, vehicle_id:STRING, avg_speed:FLOAT, coordinates:STRING, is_Ticketed:BOOLEAN, license_plate:STRING, image_url:STRING',
                    create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                    write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
            )
                    
        )
        

        (
            processed_data.non_fined_vehicles 
                | "Encode non_fined_vehicles to Bytes" >> beam.Map(lambda x: json.dumps(x).encode("utf-8"))
                | "Write non_fined_vehicles to PubSub" >> beam.io.WriteToPubSub(f'projects/{args.project_id}/topics/{args.output_topic}')
        )
        

if __name__ == '__main__':

    # Set Logs
    logging.getLogger().setLevel(logging.INFO)

    logging.info("The process started")

    # Run Process
    run()