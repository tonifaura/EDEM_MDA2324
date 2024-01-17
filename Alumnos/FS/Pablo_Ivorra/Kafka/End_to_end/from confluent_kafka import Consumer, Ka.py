from confluent_kafka import Consumer, KafkaError

# Configuración del consumidor
config = {
    'bootstrap.servers': 'localhost:9092',  # Cambia esto a tus servidores Kafka
    'group.id': 'mygroup',  # Cambia esto a tu grupo de consumidores
    'auto.offset.reset': 'earliest',  # Comienza desde el principio si no se encuentra un offset
}

# Crear una instancia del consumidor
consumer = Consumer(config)

# Suscribirse a un tema
consumer.subscribe(['mytopic'])  # Cambia esto a tu tema