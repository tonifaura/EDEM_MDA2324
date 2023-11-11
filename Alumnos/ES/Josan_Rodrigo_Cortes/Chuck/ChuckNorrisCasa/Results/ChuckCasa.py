

import requests
import json
import time
"""
url = "https://api.chucknorris.io/jokes/random"
respuesta = requests.get(url)
value=respuesta.json()
fraseChuck:str =value["value"]
"""
url = "https://api.chucknorris.io/jokes/random"

numeroFrases=0

while numeroFrases<=3:

    time.sleep(1)
    respuesta = requests.get(url)
    datos=respuesta.json()
    fraseChuck:str =datos["value"]  
    numeroFrases+=1
    f = open("ChuckCasa.txt", "a")
    f.write( str(numeroFrases) +" " + fraseChuck + "\n")
    f.close()

print("Ya he salido del bucle")

#ahora hay que contar cada palabra y decir cuantas palabras hay de cada longitud

texto= open("ChuckCasa.txt","r")

for linea in texto:
   
   palabras=linea.split()
   

print(palabras)
   #listaPalabras.append(frases)
   #alabrasSueltas=[]

   #for frases in listaPalabras:
   #    palabras=frases.split #tiene buena pinta, ahora hay que dividir de la lista listapalabras en palabras sueltas para poder añadirlas.



"""
datos = []
with open('test.txt', 'r') as rawData:
    next(rawData)  # Leer y descartar primera linea
    for linea in rawData:  # Procesar las restantes
      linea=linea.rstrip('\n') #este remueve el salto de linea
      dato=float(linea.split(",")[-1])
      datos.append(dato)

"""