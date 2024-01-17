import requests
import json

def creacion_streams():
    # URL del servidor KSQL
    ksql_url = "http://ksql-server:8088/ksql"

    # Headers para la solicitud
    headers = {
        "Content-Type": "application/vnd.ksql.v1+json",
        "Accept": "application/vnd.ksql.v1+json"
    }

    def send_ksql_command(command):
        payload = {"ksql": command, "streamsProperties": {}}
        response = requests.post(ksql_url, headers=headers, data=json.dumps(payload))
        if response.status_code == 200:
            print(f"Comando '{command}' ejecutado con éxito.")
            print(response.json())
        else:
            print(f"Error al ejecutar el comando '{command}'")
            print(response.text)

    # CREACIÓN DE STREAMS EN KSQL
    commands = [
        # Crear un stream basado en tu API
        "CREATE STREAM crypto_stream ("
        "   timestamp VARCHAR, "
        "   btc_dominance DOUBLE, "
        "   active_cryptocurrencies INT, "
        "   active_exchanges INT, "
        "   active_market_pairs INT, "
        "   total_market_cap DOUBLE, "
        "   total_volume_24h DOUBLE, "
        "   total_volume_24h_reported DOUBLE, "
        "   altcoin_market_cap DOUBLE, "
        "   altcoin_volume_24h DOUBLE, "
        "   altcoin_volume_24h_reported DOUBLE"
        ") WITH (KAFKA_TOPIC='T1_Crypto_Data', VALUE_FORMAT='JSON');",
        
        # Crear un stream para datos específicos
        "CREATE STREAM altcoin_stream AS SELECT "
        "   timestamp, "
        "   altcoin_market_cap AS market_cap, "
        "   altcoin_volume_24h AS volume_24h "
        "FROM crypto_stream;",
        
        # Ejemplo de consulta
        "CREATE TABLE top_altcoins AS SELECT "
        "   timestamp, "
        "   altcoin_market_cap AS market_cap, "
        "   altcoin_volume_24h AS volume_24h "
        "FROM crypto_stream "
        "WHERE altcoin_market_cap > 1000000000;"
    ]

    for command in commands:
        send_ksql_command(command)
