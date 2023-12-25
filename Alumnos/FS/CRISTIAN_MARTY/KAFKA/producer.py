import time
from json import dumps
from confluent_kafka import Producer
from faker import Faker
from datetime import datetime, timedelta

faker = Faker('es_ES')

# Configuración del productor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config)

# Send 100 messages where the key is the index and the message to send is "test message - index"
# the topic name is myTopic

topic_kafka = 'meteorologia'

for e in range(1000):
    fecha_hoy = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    fecha_hora_simulada = fecha_hoy + timedelta(hours=faker.random_int(min=0, max=23),
                                                minutes=faker.random_int(min=0, max=59),
                                                seconds=faker.random_int(min=0, max=59))
    
    estacion_meteorologica = {
        "id_registro": faker.uuid4(),  # Código alfanumérico aleatorio de 16 dígitos
        "fecha_hora": fecha_hora_simulada.strftime("%Y-%m-%d %H:%M:%S"),  # Incluye minutos y segundos
        "nombre_estacion": faker.word(),  # Nombre de la estación atmosférica
        "nombre_ciudad": faker.city(),
        "temperatura": faker.random_int(min=-10, max=30),
        "humedad": faker.random_int(min=0, max=100),
        "velocidad_viento": faker.random_int(min=0, max=20),
        "direccion_viento": faker.random_element(elements=("Norte", "Sur", "Este", "Oeste")),
        "presion_atmosferica": faker.random_int(min=950, max=1050),
        "precipitacion": faker.random_int(min=0, max=20),
        "visibilidad": faker.random_int(min=1, max=10),  # Ejemplo de visibilidad en km
        "nubosidad": faker.random_int(min=0, max=100),  # Ejemplo de nubosidad en porcentaje
        "radiacion_solar": faker.random_int(min=0, max=1000),  # Ejemplo de radiación solar en W/m^2
        "indice_uv": faker.random_int(min=0, max=10),  # Ejemplo de índice UV
        "precipitacion_acumulada": faker.random_int(min=0, max=100),  # Ejemplo de precipitación acumulada en mm
    }
    data_str = dumps(estacion_meteorologica)  # Serialize dictionary to a string
    data_bytes = data_str.encode('utf-8')  # Encode string to bytes
    key = str(e).encode('utf-8')
    producer.produce(topic=topic_kafka, value=data_bytes, key=key)  # Send bytes
    print("Sending data: {} to topic {}".format(estacion_meteorologica, topic_kafka))
    time.sleep(1)

# After your loop where you send messages:
producer.flush()

# Optionally, you can check if there are any messages that failed to be delivered:
if producer.flush() != 0:
    print("Some messages failed to be delivered")
