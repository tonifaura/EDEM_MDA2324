import requests
import json
import time
print("Hola Mundo")

url = "https://api.chucknorris.io/jokes/random"
f = open("results.txt","a")

#Crea una solicitud para la api
#Bucle

count = 0
while count < 10:
#Print de la respuestas
    time.sleep(3)
    response = requests.get(url)
    la_broma = response.json()["value"]
    count += 1
    #print(la_broma)
    f.write(la_broma + "\n")
