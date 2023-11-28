import random
# 1 Necesitamos un bucle en que iteremos las palabras: listar la fila del csv
# 2 Comparar

#ver de que forma puedo comparar letra por letra, atacar cada hueco por si solo
# iterar contra la palabra toda la lista.

palabras=["cosquillas", "japonesa", "aullar", "amistad", "matrimonio","obligatorio", "trenza", "aldea", "peinado", "principal"]
# palabras=["aa"]
totalintentos=0

for palabra in palabras:
    abcedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    huecos=len(palabra)
    longitudABC=len(abcedario)
    intentos=0
    while huecos>0:        
        letraAzar= random.choice(abcedario)
        for letra in palabra:
            veces = palabra.count(letraAzar)
            if veces>=1:               
                huecos-=veces
                intentos+=1
                abcedario.remove(letraAzar)
                break
            else:
                abcedario.remove(letraAzar)
                intentos+=1
                break  
    totalintentos+=intentos 
print(totalintentos)
    
        
