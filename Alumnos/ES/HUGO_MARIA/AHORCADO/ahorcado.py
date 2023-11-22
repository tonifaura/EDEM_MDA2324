import random
# 1. Agregando el diccionario

abecedario2 = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
abecedario = ['E', 'A', 'O', 'I', 'S', 'N', 'R', 'L', 'U', 'D', 'T', 'C', 'M', 'P', 'B', 'G', 'V', 'Y', 'Q', 'H', 'F', 'J', 'Ñ', 'Z', 'X', 'K', 'W']


#PASO 2
with open("palabras.csv", "r") as archivo:
    palabras = archivo.read().splitlines()

#print(palabras)

#PASO 3
#for palabra in palabras:
#    letras = len(palabra)
#    print(letras)

intento= 0

for palabra in palabras:
    longitud = len(palabra)
    for letra in abecedario:
        intento += 1
        contador = palabra.count(letra)


print(intento)





#total_recorrido = 0
#total_no_recorrido= 0

#for palabra in lista_palabras:
