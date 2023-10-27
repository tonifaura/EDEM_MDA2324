#Juego
#elegir palabras 

listaPalabras =  ['manzana']
import string
abecedario = string.ascii_lowercase
intentoMal = 1

for palabra in listaPalabras:
   print (palabra)
   for letra in abecedario:
     if (letra in palabra):
        intentoMal += intentoMal
     else:
        intentoMal += intentoMal

print(intentoMal)

