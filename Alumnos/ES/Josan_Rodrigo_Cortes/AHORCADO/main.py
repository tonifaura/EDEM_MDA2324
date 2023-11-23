
import random
""" 1 leer palabras del csv
2 transformar a lista
3 for cada palabra en listapalabras
5 contar letras
3 mientras haya huecos
7 dame una letras que no haya salido
8 si letra en palabras:restar las apariciones letras
9 contar intentos """
#Ahorcado, apartir de una lista csv de palabras adivinarlas
""" import pandas as pd

palabras=df = pd.read_csv('palabras.csv', sep=',') """
palabras=["Cosquillas", "Japonesa", "Aullar", "Amistad", "Matrimonio","Obligatorio", "Trenza", "Aldea", "Peinado", "Principal"]


# 1 Necesitamos un bucle en que iteremos las palabras: listar la fila del csv
# 2 Comparar

#ver de que forma puedo comparar letra por letra, atacar cada hueco por si solo
# iterar contra la palabra toda la lista.
totalintentos=0
for palabra in palabras:
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    huecos=len(palabra)
   
    intentos=0
    while huecos>0:
        
        letraAzar= random.choice(letras)

        veces = palabra.count(letraAzar)

        huecos-=veces

        letras.remove(letraAzar)

        intentos+=1
    totalintentos+=intentos
    print(intentos)
    print("Palabra acertada")






    



    
    


