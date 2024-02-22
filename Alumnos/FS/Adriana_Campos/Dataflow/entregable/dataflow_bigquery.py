import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
from apache_beam.io.gcp.bigquery import WriteToBigQuery
from apache_beam.io.gcp.internal.clients import bigquery
import json
from datetime import datetime


project_id = 'woven-justice-411714'
topic_name= 'camara-output'
table_name = "woven-justice-411714:ejemplo.camara"
suscripcion ='projects/woven-justice-411714/subscriptions/camara-output-sub'
bucket_name='bucket-camara'

# Recibe datos
def decode_message(msg):
    # Lógica para decodificar el mensaje y cargarlo como JSON
    output = msg.decode('utf-8')
    json_data = json.loads(output)
    print(f"JSON guardado en BigQuery: {json_data}")
    return json_data

# Obtiene la hora actual en formato UTC
current_time_utc = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]

class DecodeMessage(beam.DoFn):
    def process(self, element):
        output = element.decode('utf-8')
        json_data = json.loads(output)
        print(f"JSON guardado en BigQuery: {json_data}")
        return [json_data]
    


#{"radar_id": "adriana", "vehicle_id": "yaZ67o", "avg_speed": 32.665949301019054, "coordinates": [39.4699, -0.3763], "is_Ticketed": false, "license_plate": null}

# Nueva definición del esquema para BigQuery
new_table_schema_personas = bigquery.TableSchema()
new_table_fields_personas = [
    bigquery.TableFieldSchema(name='radar_id', type='STRING', mode='NULLABLE'),
    bigquery.TableFieldSchema(name='vehicle_id', type='STRING', mode='NULLABLE'),
    bigquery.TableFieldSchema(name='speed', type='FLOAT', mode='NULLABLE'),
    bigquery.TableFieldSchema(name='coordinates', type='STRING', mode='NULLABLE'),
    bigquery.TableFieldSchema(name='is_Ticketed', type='BOOLEAN', mode='NULLABLE'),
    bigquery.TableFieldSchema(name='license_plate', type='STRING', mode='NULLABLE'),
]
new_table_schema_personas.fields.extend(new_table_fields_personas)

options = PipelineOptions(
    streaming=True,
    runner='DataflowRunner',
    project=project_id,
    region='europe-west4',
    temp_location=f"gs://{bucket_name}/tmp",
    staging_location=f"gs://{bucket_name}/staging",
    enable_streaming_engine=True
)

with beam.Pipeline(options=options) as p:
    #coches:
    data = (
        p
        | "LeerDesdePubSub2" >> beam.io.ReadFromPubSub(subscription=suscripcion)
        | "decodificar_msg2" >> beam.ParDo(DecodeMessage())
        | "escribir2" >> beam.io.WriteToBigQuery(
            table=table_name,
            schema=new_table_schema_personas,
            create_disposition=beam.io.BigQueryDisposition.CREATE_NEVER,
            write_disposition=beam.io.BigQueryDisposition.WRITE_APPEND
        )
    #data | "Print Result" >> beam.Map(print)
    )
