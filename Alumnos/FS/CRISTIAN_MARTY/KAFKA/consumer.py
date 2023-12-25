import time
from confluent_kafka import Consumer, Producer, KafkaError
from json import dumps, loads

#----- Configuración del consumidor ---------
config_consumer = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config_consumer)

# Topico_Consumidor
topic_consumer = 'meteorologia'
consumer.subscribe([topic_consumer])

# ------Configuración del productor-------
config_producer = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'python-producer'
}

# Crear un productor
producer = Producer(config_producer)
topic_producer = 'meteorologia_valencia'

# Leer la lista de ciudades desde el archivo externo
with open('ciudades_filtradas.txt', 'r') as file:
    ciudades_deseadas = [line.strip().lower() for line in file]

def ciudad_es_deseada(nombre_ciudad):
    return nombre_ciudad.lower() in ciudades_deseadas

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print("No hay más mensajes en esta partición.")
            else:
                print("Error al recibir mensaje: {}".format(msg.error()))
        else:
            # Procesar el mensaje recibido.
            msg_value_str = msg.value().decode('utf-8')

            # Deserializar el mensaje JSON
            msg_json = loads(msg_value_str)

            # Filtrar los mensajes donde el nombre_ciudad esté en la lista de ciudades deseadas
            if 'nombre_ciudad' in msg_json and ciudad_es_deseada(msg_json['nombre_ciudad']):
                # Serializar el mensaje filtrado de nuevo a cadena JSON
                filtered_msg_str = dumps(msg_json)
                filtered_msg_bytes = filtered_msg_str.encode('utf-8')

                # Enviar el mensaje filtrado al nuevo tópico
                producer.produce(topic=topic_producer, value=filtered_msg_bytes)
                print("Enviando datos a {} al tópico {}".format(filtered_msg_str, topic_producer))

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al detener la aplicación Python
    consumer.close()
