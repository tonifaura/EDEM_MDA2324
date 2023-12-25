import time
from confluent_kafka import Consumer, KafkaError
from json import loads

# Configuración del consumidor
config_consumer = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'python-consumer-group',
    'auto.offset.reset': 'earliest'
}

# Crear un consumidor
consumer = Consumer(config_consumer)

# Topico_Consumidor
topic_consumer = 'METEOROLOGIA_BI_STREAM'
consumer.subscribe([topic_consumer])

# Datos en tiempo real
city_data = {}

def print_bar(value, max_value):
    bar_length = 20
    scaled_value = int((value / max_value) * bar_length)
    return '*' * scaled_value + '-' * (bar_length - scaled_value)

# Loop infinito de consumo de mensajes del topic
try:
    while True:
        msg = consumer.poll(1.0)  # Lee nuevos mensajes cada 1 segundo

        if msg is not None:
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

                # Actualizar datos en tiempo real
                city = msg_json['NOMBRE_CIUDAD']
                temperature = msg_json.get('TEMPERATURA', 0)
                humidity = msg_json.get('HUMEDAD', 0)
                wind_speed = msg_json.get('VELOCIDAD_VIENTO', 0)

                city_data[city] = {'Temperature': temperature, 'Humidity': humidity, 'Wind Speed': wind_speed}

                # Limpiar la consola
                print("\033c")

                # Imprimir gráfico de barras en tiempo real
                for city, data in city_data.items():
                    print(f"{city}:")
                    print(f"   Temperatura: {print_bar(data['Temperature'], 40)} {data['Temperature']}°C")
                    print(f"   Humedad:    {print_bar(data['Humidity'], 100)} {data['Humidity']}%")
                    print(f"   Viento:  {print_bar(data['Wind Speed'], 40)} {data['Wind Speed']} km/h")
                    print("\n")

                # Esperar antes de la próxima actualización
                time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    # Cerrar el consumidor al detener la aplicación Python
    consumer.close()
