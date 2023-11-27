import random
# 1 Necesitamos un bucle en que iteremos las palabras: listar la fila del csv
# 2 Comparar

#ver de que forma puedo comparar letra por letra, atacar cada hueco por si solo
# iterar contra la palabra toda la lista.

# palabras=["cosquillas", "Japonesa", "Aullar", "Amistad", "Matrimonio","Obligatorio", "Trenza", "Aldea", "Peinado", "Principal"]
palabras=["cosquillas"]
totalintentos=0

intentos=0

for palabra in palabras:
    abcedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    
    letrasAdivinadas=[]
    huecos=len(palabra)
    
    while huecos>0:
        
        
        letraAzar= random.choice(abcedario)
        
        
        for letra in palabra:
            veces = palabra.count(letraAzar)
            if letra==letraAzar:
                
                huecos-=veces
                
                intentos+=1
                abcedario.remove(letraAzar)
                letrasAdivinadas.append(letra)
                break
            else:
                intentos+=1
                break
      
print(intentos)
    
        
