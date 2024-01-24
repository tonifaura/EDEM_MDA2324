# END2END - KAFKA para la Gestión de Carteras de Criptomonedas con la API de Coinbase (Simplificado)

## Proyecto
En este proyecto, utilizamos la API de Coinbase para monitorear carteras de criptomonedas y crear alertas de precios en tiempo real. Utilizamos Apache Kafka para gestionar los datos en tiempo real y KSQL para procesarlos.


## Arquitectura
La arquitectura de nuestro sistema implica varios componentes clave:

- API de Coinbase: Obtenemos datos de inversiones en criptomonedas.
- Base de Datos MySQL: Almacenamos los datos de la API de Coinbase.
- Kafka: Manejamos el flujo de datos en tiempo real.
- Uso de Kafka: Procesamos datos en tiempo real y generamos alertas.

**Uso de Kafka:**

- Productor a "Pricelist": Enviamos datos a un tópico de Kafka llamado "Pricelist".
- Consumidores para Procesamiento: Leemos datos de "Pricelist", los procesamos y filtramos.
- Enrutamiento de Datos: Los datos procesados se envían a los tópicos "Alertas" o "Variaciones de Precios".
- KSQL para Filtrado: Usamos KSQL para filtrar más datos en los tópicos "Alertas" y "Variaciones de Precios".
- Visualización de Datos: Mostramos los resultados en el terminal de Visual Studio.

## Escenario: Identificación de Oportunidades de Compra
Nos enfocamos en identificar oportunidades de compra basadas en variaciones de precios y umbrales establecidos.

## Despliegue de la Aplicación
Para desplegar la aplicación, siga estos pasos:

1. Ejecute `docker-compose up -d` para iniciar los contenedores.
2. Cree una tabla en la base de datos.
3. Ejecute `python3 model/data/data_ingestion.py` para ingresar datos.
4. Si hay problemas con el contenedor Kafka, use `docker ps` para obtener el nombre o ID del contenedor y luego `docker exec -it [NOMBRE_O_ID_DEL_CONTENEDOR_KAFKA] bash` para ingresar al bash del contenedor y crear los tópicos.


