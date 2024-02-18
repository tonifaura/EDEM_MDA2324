python EDEM_Dataflow_Streaming_Pipeline.py \
    --project_id woven-justice-411714 \
    --input_subscription <YOUR_INPUT_PUBSUB_SUBSCRIPTION_NAME> \
    --output_topic <YOUR_OUTPUT_PUBSUB_TOPIC_NAME> \
    --radar_id 123 \
    --cars_api <API_URL>



python generator.py \
    --project_id woven-justice-411714 \
    --topic_name projects/woven-justice-411714/topics/camera\
    --initial_coordinates <COORDINATES_INITIAL_POINT> \
    --final_coordinates <COORDINATES_FINAL_POINT>