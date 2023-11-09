

import requests
import time
import json

print("Hello World")

file= open("Results.txt","a")     #./ChuckNorris/Results/"chuck.txt","a"

url= "https://api.chucknorris.io/jokes/random"

for i in range (20):
    print(i)
    
    time.sleep(2)

    #Crear una solicitud para la API
    response = requests.get(url)

    #Accede al json clave: "value" (diccionario)
    joke= response.json()["value"]

    #Escribe el Chiste en el txt

    file.write(joke + "\n")

#while (True):
    #time.sleep(5)
