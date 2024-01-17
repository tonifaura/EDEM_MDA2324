from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
consumer_config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto con la dirección de tu servidor Kafka
    'group.id': 'my_consumer_group',  # Cambia esto al ID de tu grupo de consumidores
    'auto.offset.reset': 'earliest'
}

# Crea una instancia del consumidor
consumer = Consumer(consumer_config)

# Suscribe al topic "marketcap"
consumer.subscribe(['marketcap'])

try:
    while True:
        # Lee un mensaje de Kafka
        msg = consumer.poll(1.0)

        if msg is None:
            continue

        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Llegó al final de la partición')
            else:
                print(f'Error en el mensaje: {msg.error()}')
        else:
            # Mostrar el mensaje sin procesar
            print("Mensaje recibido:", msg.value().decode("utf-8"))

except KeyboardInterrupt:
    pass

finally:
    # Cierra el consumidor
    consumer.close()
