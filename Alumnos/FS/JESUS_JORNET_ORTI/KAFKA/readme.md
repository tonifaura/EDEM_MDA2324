# Kafka - Caso de uso

Para este caso de uso hemos simulado cómo sería una recogida de datos de la calidad del aire en la ciudad de València.

## Imagen de todo esto funcionando
![Imagen de Kafka en terminal](KAFKA/Imagen/captura.png)

### Docker compose
Empezamos haciendo docker-compose up -d del archivo docker-compose.yml.

### Producer
Para esto primero hemos hecho un producer.py que genera los datos de:
- Station_id
- pm10
- pm2_5
- no2
- timestamp

### Consumer
Esos datos se recogen a través de un consumer.py

### KSQL
Posteriormente en una terminal corremos KSQL con el siguiente código en terminal:
```ruby
docker exec -it entregable-ksql-cli-1 ksql http://kafka-ksql-server-1:8088
```

Generamos el siguiente Stream:
```ruby
CREATE STREAM air_quality_stream (
    station_id STRING,
    pm10 DOUBLE,
    pm2_5 DOUBLE,
    no2 DOUBLE,
    timestamp STRING,
    calidad_aire STRING
) WITH (
    KAFKA_TOPIC='processed_air_quality',
    VALUE_FORMAT='JSON'
);
```

Y luego vemos los datos con la siguiente query:
```ruby
SELECT * FROM air_quality_stream EMIT CHANGES LIMIT 10
```