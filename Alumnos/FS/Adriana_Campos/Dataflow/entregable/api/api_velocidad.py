import requests

# URL de la Overpass API
url = 'https://overpass-api.de/api/interpreter'

# Consulta de ejemplo: Obtener nodos y caminos en un área específica
query = """
[out:json];
area["name"="San Francisco"]->.a;
(
  node(area.a)[highway];
  way(area.a)[highway];
);
out center;
"""

# Parámetros de la solicitud
params = {
    'data': query
}

# Realiza la solicitud a la Overpass API
response = requests.post(url, data=params)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    # Procesa y utiliza los datos obtenidos
    print(data)
else:
    print(f"Error en la solicitud: {response.status_code}")
    print(response.text)
