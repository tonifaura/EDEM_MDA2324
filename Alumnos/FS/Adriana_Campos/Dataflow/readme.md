# CASO DE USO

El Ayuntamiento de Nueva York, del que formamos parte de su equipo de Datos, ha identificado un aumento significativo en el número de accidentes de tráfico en el distrito de Manhattan debido a la velocidad de los vehículos. Para abordar esta cuestión, se ha decidido implementar cámaras dotadas de Inteligencia Artificial para monitorizar la velocidad de los vehículos en tramos concretos.

*Retos empresariales*
  
- Cada cámara se instalará en un tramo concreto y deberá calcular la velocidad media de cada vehículo.
- La velocidad promedio en el tramo no deberá exceder las 25 millas por hora (40 km/h).
- Se debe capturar una imagen , obtener el número de placa y almacenar la foto analizada de todos los vehículos multados.
- 
Requisitos del caso

- Los datos captados por las diferentes cámaras deberán ser enviados al tema previsto durante la clase para la adecuada visualización de los datos.

- Los datos también deben almacenarse en el Data Warehouse para su posterior análisis por parte del equipo de Analistas. [Asignación de tareas] .

- El mensaje de notificación de multas ahora debería incluir la URL del Google Cloud Storage Bucket donde se almacena la imagen del vehículo , para verificar que el modelo ha capturado correctamente el texto de la matrícula. [Tarea (opcional)] .

# Indicaciones


# Generador 


```
python generador.py \
    --project_id woven-justice-411714 \
    --topic_name camera \
    --initial_coordinates "37.7749,-122.4194"  \
    --final_coordinates "34.0522,-118.2437"
```

```
python Dataflow_Streaming_Pipeline.py \
    --project_id woven-justice-411714  \
    --input_subscription 'projects/woven-justice-411714/subscriptions/camera-sub' \
    --output_topic 'projects/woven-justice-411714/topics/camara-output' \
    --radar_id adriana \
    --cars_api https://console.cloud.google.com/storage/browser/output-camara
```


# DATAFLOW Pipeline
