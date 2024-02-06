# Use Case: Weather service history
## Target of Application (Business Point of View): 
Provide real-time weather data processing to generate historical records, enabling better analysis and forecasting. In this brief analysis, temperature, humidity and wind speed will be examined throught differens locations from Spain.

## Architecture
    1. API-get from AEMET to get recent data of the weather conditions from Spain.
    2. Producer.py ingest the json messages into a kafka topic
    3. Kafka server (where kafka topic is <topic_tiempo>)
    4. Consumer.py consum these messages that contains the following info: 
            {
            "humidity": 44,
            "location": "ALFORJA",
            "temperature": 18.8,
            "timestamp": "2024-02-05T11:00:00",
            "wind_speed": 3.6
            }
    5. KSQL server to make KSQL queries