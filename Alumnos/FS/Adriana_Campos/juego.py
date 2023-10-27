#Juego
#elegir palabras 
import pandas as pd

listaPalabras= ['remedio', 'pronunciar', 'manejar', 'ley','elefante']
#listaPalabras= pd.read_csv('/Users/adrianacamposnarvaez/Documents/GitHub/EDEM_MDA2324/Alumnos/FS/#Adriana_Campos/palabras.txt')

import string
abecedario = string.ascii_lowercase
intento = 0
coicide = 0

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
           intento = intento+1
    

print(intento)

