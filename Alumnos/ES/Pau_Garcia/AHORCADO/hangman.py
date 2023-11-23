# Importamos librerias necesarias. 
import pandas as pd
import random
# Leemos el archivo con las palabras
words = pd.read_csv("palabras.csv", sep=',', header=0)

# Transformamos a lista
list_words = []
for palabra in words:
    list_words.append(palabra)

### LETRAS ALEATORIAS
# # Iteramos para resolver cada palabra
# intentos=0
# for word in list_words:
#     # Restauramos lista dado que la hemos manipulado durante la resolución
#     letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     #  Contamos letras en variable gap 
#     gaps = len(word)
#     trials = 0
#     while gaps>0:
#         # Elige una letra aleatoria de la lista letters
#         letter_chosen = random.choice(letters)
#         # Cuenta cuántas veces está la letra en la palabra
#         times = word.count(letter_chosen)
#         # gaps actualiza y quita times
#         gaps -= times
#         # Actualizar lista
#         letters.remove(letter_chosen)
#         trials += 1
#     intentos+=trials
# print(intentos)


### LETRAS ORDENADAS POR FRECUENCIA
# Iteramos para resolver cada palabra
intentos=0
for word in list_words:
    # Restauramos lista dado que la hemos manipulado durante la resolución
    letters = ['e', 'a', 'o', 'i', 's', 'n', 'r', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'f', 'h', 'j', 'z', 'x', 'k', 'w']
    #  Contamos letras en variable gap 
    gaps = len(word)
    trials = 0
    while gaps>0:
        for let in letters:
            if gaps>0:

        # Cuenta cuántas veces está la letra en la palabra
                times = word.count(let)
        # gaps actualiza y quita times
                gaps -= times
                trials += 1
            else:
                break
            
    intentos+=trials
print(intentos)







