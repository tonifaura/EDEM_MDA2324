

import requests
import json
import time

url = "https://api.chucknorris.io/jokes/random"
respuesta = requests.get(url)
value=respuesta.json()
fraseChuck:str =value["value"]

numeroFrases=0
while numeroFrases<5:
    time.sleep(2)
    numeroFrases+=1
    f = open("ChuckCasa.txt", "a")
    f.write(str(numeroFrases)+ " ChuckCasa.txt")





print(fraseChuck)