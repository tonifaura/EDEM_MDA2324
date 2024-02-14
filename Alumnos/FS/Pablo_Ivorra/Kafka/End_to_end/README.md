# END2END - KAFKA para la Gestión de Carteras de Criptomonedas con la API de Coinbase 

## Proyecto
El caso de uso de esta aplicación es la monitorización en tiempo real de los datos de una cartera del mercado de criptomonedas. La aplicación puede ser utilizada por analistas financieros, traders o cualquier persona interesada en seguir de cerca los cambios en su cartera de cryptos. Al consumir datos en tiempo real del topic "marketcap" en Kafka, la aplicación puede procesar y mostrar información actualizada sobre el capital total del mercado, el volumen de operaciones, el capital de mercado de altcoins, etc.

**Uso de Kafka:**

- Productor a "Pricelist": Enviamos datos a un tópico de Kafka llamado "marketcap".
- Consumidores para Procesamiento: Leemos datos de "Pricelist", los procesamos y filtramos.
- Enrutamiento de Datos: Los datos procesados se envían a los tópicos "Alertas" o "Variaciones de Precios".
- KSQL para Filtrado: Usamos KSQL para filtrar más datos en los tópicos "Alertas" y "Variaciones de Precios".
- Visualización de Datos: Mostramos los resultados en el terminal de Visual Studio.

## Escenario: Identificación de Oportunidades de Compra
Nos enfocamos en identificar oportunidades de compra basadas en variaciones de precios y umbrales establecidos.


