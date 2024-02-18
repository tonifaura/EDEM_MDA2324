
import googlemaps

# Reemplaza 'TU_CLAVE_DE_API' con tu propia clave de API de Google Cloud
gmaps = googlemaps.Client(key='AIzaSyDO-oBaaU8isj6Enj0kBvYiPousCR_U_d0')

# Dirección que deseas geocodificar
direccion = '1600 Amphitheatre Parkway, Mountain View, CA'

# Realiza la solicitud de geocodificación
resultado = gmaps.geocode(direccion)

# Imprime la información de geocodificación
if resultado:
    ubicacion = resultado[0]['geometry']['location']
    print(f"Latitud: {ubicacion['lat']}, Longitud: {ubicacion['lng']}")
else:
    print("No se encontró la ubicación.")
