""" Ejercicio 3
Realiza una petición HTTPs a la ruta https://randomuser.me/api y muestra por consola el nombre y los
 apellidos retornados por la API
 """

import requests
import json

url = "https://randomuser.me/api"

respuesta = requests.get(url)


datos=respuesta.json()
resultado=datos["results"]

    for dato in datos["results"]:
        print(dato[0]["name"])


print(datos)
# fraseChuck:str =datos["value"]  

