import requests

# URL de la HERE Traffic API
url = 'https://traffic.ls.hereapi.com/traffic/6.3/incidents.json'

# Parámetros de la solicitud (reemplaza con tus propios parámetros)
params = {
    'apiKey': 'z-dZWKNr8aGa8ik2olu_PXHx768VB0aY8_2IzFA505Y',  # Reemplaza con tu propia clave de API de HERE
    'bbox': '52.5,13.4;52.6,13.5',  # Ejemplo de cuadro delimitador (lat,lng;lat,lng)
}

# Realiza la solicitud a la API de HERE Traffic
response = requests.get(url, params=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Procesa y utiliza los datos de tráfico según la respuesta
    print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
