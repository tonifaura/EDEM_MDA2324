from confluent_kafka.admin import AdminClient, NewTopic

# Configura la conexión con el servidor Kafka
bootstrap_servers = 'localhost:9092'  # Cambia esto con la dirección de tu servidor Kafka

# Crea una instancia del administrador de Kafka
admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

# Define la configuración del nuevo topic
new_topic = NewTopic('marketcap', num_partitions=1, replication_factor=1)

# Crea el topic utilizando el administrador
admin_client.create_topics([new_topic])

print(f"Topic 'marketcap' creado exitosamente.")
