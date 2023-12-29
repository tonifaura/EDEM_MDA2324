# Proyecto Kafka
Para utilizar KAFKA y aprovechar la virtud de mensajería en tiempo real, se ha escogido un caso de uso que pueda encajar en esa necesidad. 
El caso de uso es el sistema de alertas de emergencias y 112.

# Proceso general
El proceso entero de generación de información, producción de mensajería y consumo se ha dockerizado, de tal forma que el docker-compose ya debería levantar todo el proceso. 

Este, se puede ver en el siguiente flujograma:

![Alt text](<Flujograma del proceso.jpeg>)

Los avisos por emergencia llegan a un Topic de entrada, estos se re-dirigen en función del grado de urgencia hacia dos topics distintos. Los casos No Urgentes son re-dirigidos a sus respectivas áreas. Aquellos que sí son urgentes, son analizados. Si necesitan un médico (o el cuerpo necesario es Médicos), se consulta la dirección de destino para poder enviar la ambulacia y se envía al Topic de Sanitarios 112. En caso de no necesitar ambulancia, se envían al Topic del Centro de Mando.


No obstante, el proceso de consumo, almacenamiento y descarga de los resultados en formato JSON se ha realizado de forma externa por facilidad y flexibilidad en cuanto a la carpeta de descarga.

# Proceso detallado e inventario de archivos de la carpeta:
* **Dockerfile** - Almacena la información para generar la imagen que copie todos los scripts necesarios y arranque el script main.py
* **Docker-compose** - Contiene todos los contenedores necesarios para ejecutar el proceso (sin incluir la descarga y visualización de resultados en Power BI, partes que, por facilidad y flexibilidad, están por fuera del proceso.)
* **KP_1_Definicion_clase**: Se define los atributos y caracteristicas de la clase "Emergencia"
* **KP_2_Creacion_topics**: Se crean los topics necesarios para el flujo de información.
* **KP_3_Creacion_streams_KSQ**L: Se crean los STREAMS de re-dirección de información mediante KSQL
* **KP_4_Productor_inicial**: Se generan los registros en base a la definición de la clase y se envían al Topic asignado.
* **KP_5_Consumidor_y_productor**: Consume la información del Topic T2.Centro_112, se comprueba si necesita un médico y en caso afirmativo, se añade una dirección aleatoria. Posteriomente, se produce la información y se envía al Topic T2.1_Sanitarios_112
* **KP_6_Descargar_CVS**: Descarga la información en formato json. Se ejecuta por fuera del docker-compose.
* **TOTAL_AVISOS**: json con la información de todos los avisos recibidos en el Topic 1 descargada tras haber ejecutado el proceso.
* **TOTAL_AVISOS_SANITARIOS_112**: json con la información de todos los avisos médicos. Este fichero sirve para comprobar que todo el proceso se ha ejecutado de forma correcta. Se puede comprobar que los avisos en este fichero también existen en el general, solo que en ese no incluyen la dirección.
* **Analisis_emergencias.pbix** : PowerBi con una visualización sencilla e ilustrativa de cómo se podrían reflejar los resultados.
* **Main.py**: Para buscar la mayor facilidad y lectura, este fichero únicamente contiene importaciones y las cuatro funciones globales para ejecutar el proceso.
* **Requirements.txt**: Librerias externas utilizadas y necesarias para arrancar el proceso.

NOTA: Adiconalmente, la carpeta cuenta con funcionalidades auxiliares que han sido necesarias en el proceso de creación, como son Borrar Queries emitidas de SQL; un consumer básico, Comprobar Topics "NO INTERNOS" activos, su borrado etc.

# Otras consideraciones:
* Se ha tenido especial cuidado en la generación de información para que sea lo más realista posible, buscando que exista coherencia entre los eventos, los cuerpos asignados, y la urgencia. (No tiene sentido que el grado de urgencia sea leva y se llame a los GEOS, o que haya un Atraco y se llame a un bombero)
* De la misma forma, para simular el tiempo real y la similitud con la realidad, los eventos se generan de forma cronológica (es decir, el primero mensaje siempre es de una fecha más antigua que el segundo, y así sucesivamente)
* Para garantizar que Kafka se ha levantado antes de comenzar, se ha añadido un time.sleep de 30 segundos al main.py
* Ha sido especialmente costoso la gestión de la comunicación de los productores y consumidores una vez están dockerizados ya que no se puede llamar al localhost (ya que están dentro del container)
