#Juego
#elegir palabras 
import pandas as pd
import string
import time


listaPalabras= ['remedio', 'pronunciar', 'manejar', 'ley','elefante']
#listaPalabras = pd.read_csv("/Users/adrianacamposnarvaez/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/Adriana_Campos/palabras.txt")

#abecedario = ['a','e','o','u','b','i','c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'ñ']
abecedario=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','ñ']

intento = 0
coicide = 0

inicio = time.time() 

def contar_letras_unicas(palabra):
    return len(set(palabra))

for palabra in listaPalabras:
   for letra in abecedario:
     unicas = contar_letras_unicas(palabra)
     if (unicas!=coicide):
        if (letra in palabra):
           intento = intento + 1 
           coicide = coicide + 1
        else:
           intento = intento + 1
    

fin = time.time() 
tiempo_transcurrido = fin - inicio

print (tiempo_transcurrido)
print(intento)

