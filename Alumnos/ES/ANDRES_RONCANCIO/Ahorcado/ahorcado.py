import pandas as pd

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 

with open ('palabras.csv', 'r') as archivo:
    palabras = archivo.read().splitlines()


#print(palabras)

for element in palabras:
   letras = len(element)
  # for letras in abc:
       
        
        
        
        
#en el comentario pull request..poner numero de intentos150 260
#pull request modo draf