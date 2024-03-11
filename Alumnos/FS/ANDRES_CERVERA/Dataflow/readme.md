# ENTREGABLE DATAFLOW

## OBJETIVO
Implementar cámaras equipadas con Inteligencia Artificial para monitorizar la velocidad de los vehículos en secciones específicas, y multarlos en caso necesario.

## REQUISITOS
- Cada cámara se instalará en una sección particular y deberá calcular la velocidad promedio de cada vehículo.
- La velocidad promedio en la sección no debe exceder los 25 km/h.
- Se debe capturar una imagen, obtener el número de matrícula y almacenar la foto analizada de todos los vehículos multados.

## CONDICIONES
- Los datos capturados por diferentes cámaras deben enviarse al tema proporcionado durante la clase para la correcta visualización de los datos.
- Los datos también deben almacenarse en el Data Warehouse para un análisis posterior por parte del equipo de Analistas.
- El mensaje de notificación para multas ahora debe incluir la URL del Bucket de Google Cloud Storage donde se almacena la imagen del vehículo, para verificar  que el modelo haya capturado correctamente el texto de la matrícula.

## ARQUITECTURA
![alt text](images\arquitectura.png)

## SETUP PREVIO

1. **Conectarse al entorno de GCP:**
    ```bash
    gcloud init
    gcloud auth login
    gcloud auth application-default login
    gcloud services enable dataflow.googleapis.com
    gcloud services enable pubsub.googleapis.com
    gcloud services enable vision.googleapis.com
    gcloud services enable cloudbuild.googleapis.com
    ```

2. **Crear entorno virtual y conectarse:**
    ```bash
    python -m venv andrestest
    andrestest\Scripts\activate
    ```

3. **Instalar librerías:**
    ```bash
    pip install -U -r requirements.txt
    ```


## GENERADOR
La calle sobre la que haremos el estudio es en la Avenida Lexington, una calle importante de Manhattan y muy transitada. Las coordenadas del tramo son las siguientes:

- Coordenada_ini: 40.7128° N, 73.9790° W
- Coordenada_fin: 40.7431° N, 73.9824° W

Lanzamos el generador con esa ruta y comprobamos que se vayan generando rutas de coches en esa calle en el topic de pre-procesado. Se ha añadido un fragmento de código al generador para que de manera simultánea inserte los datos del pub-sub en una tabla de BigQuery llamada pre-procesado.

### Generador

![Generador](images/generator.png)

### Pre-Procesado

![Pre-Procesado](images/pre-procesado.png)

### Tabla en BigQuery (pre-procesado)

![Tabla en BigQuery](images/pre-procesadoBQ.png)


## DATAFLOW

