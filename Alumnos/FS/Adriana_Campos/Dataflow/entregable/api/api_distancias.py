
import googlemaps

# Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API
gmaps = googlemaps.Client(key='AIzaSyDLxQ1QZC7l9aZLaVxQh9fydBSw0MMM0XI')

# Especifica los lugares de inicio y destino en Madrid
origen = "Puerta del Sol, Madrid, Spain"
destino = "Plaza Mayor, Madrid, Spain"

# Obtiene las direcciones y la información de ruta
direcciones = gmaps.directions(origen, destino, mode="driving")

# Imprime la información de las direcciones
for paso in direcciones[0]['legs'][0]['steps']:
    print(paso['html_instructions'])

# También puedes acceder a otros detalles, como la distancia y la duración
distancia = direcciones[0]['legs'][0]['distance']['text']
duracion = direcciones[0]['legs'][0]['duration']['text']
print(f"Distancia: {distancia}, Duración: {duracion}")
