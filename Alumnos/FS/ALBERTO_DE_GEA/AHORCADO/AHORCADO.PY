#PASO 1
letras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

#PASO 2
with open("palabras.txt", "r") as archivo:
    palabras = archivo.read().splitlines()

#PASO 3
#for palabra in palabras:
    #letras = len(palabra)
    #print(f'La palabra {palabra} contiene {letras} letras')

#PASO 4
letras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
palabras = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]

for palabra in palabras:
    for letra in letras:
        contador = palabra.count(letra)
        if contador > 0:
            print(f'La letra "{letra}" aparece {contador} veces en la palabra "{palabra}"')


#paso 5
letras = ["A","B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
palabras = ["REMEDIO", "PRONUNCIAR", "MANEJAR", "LEY", "ELEFANTE"]
total_contador = 0

for palabra in palabras:
    for letra in letras:
        contador = palabra.count(letra)
        total_contador += contador

print(f'Número total de veces que se utilizan las letras: {total_contador}')




   







