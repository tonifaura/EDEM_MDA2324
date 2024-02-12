# END2END - KAFKA para la Gestión de Carteras de Criptomonedas con la API de Coinbase (Simplificado)

## Proyecto
En este proyecto, utilizamos la API de Coinbase para monitorear carteras de criptomonedas y visualizar aquellas que queremos monitorizar en tiempo real. Utilizamos Apache Kafka para gestionar los datos en tiempo real y KSQL para procesarlos.

**Uso de Kafka:**

- Productor a "Pricelist": Enviamos datos a un tópico de Kafka llamado "Pricelist".
- Consumidores para Procesamiento: Leemos datos de "Pricelist", los procesamos y filtramos.
- Enrutamiento de Datos: Los datos procesados se envían a los tópicos "Alertas" o "Variaciones de Precios".
- KSQL para Filtrado: Usamos KSQL para filtrar más datos en los tópicos "Alertas" y "Variaciones de Precios".
- Visualización de Datos: Mostramos los resultados en el terminal de Visual Studio.

## Escenario: Identificación de Oportunidades de Compra
Nos enfocamos en identificar oportunidades de compra basadas en variaciones de precios y umbrales establecidos.


