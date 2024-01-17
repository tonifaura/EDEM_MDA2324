import time
from json import dumps
from confluent_kafka import Producer
import requests
# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# URL de la API
api_url = 'https://pro-api.coinmarketcap.com/v1/your-endpoint'

# Send messages based on API response
topic_kafka = 'ventas'

for e in range(100):
    # Realizar solicitud a la API
    response = requests.get(api_url)
    
    # Obtener datos de la respuesta de la API
    data = response.json()
    
    # Serializar datos a una cadena
    data_str = dumps(data)
    
    # Codificar cadena a bytes
    data_bytes = data_str.encode('utf-8')
    
    # Enviar mensaje a Kafka
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)
    
    print("Sending data: {} to topic {}".format(data, topic_kafka))
    time.sleep(1)

# Después del bucle donde envías los mensajes:
producer.flush()

# Opcionalmente, puedes verificar si hay mensajes que no se entregaron correctamente:
if producer.flush() != 0:
    print("Some messages failed to be delivered")

