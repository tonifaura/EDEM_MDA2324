# Abecedario ordenado por recurrencia de aparición:

palabras=["cosquillas", "japonesa", "aullar", "amistad", "matrimonio","obligatorio", "trenza", "aldea", "peinado", "principal"]
totalintentos=0

for palabra in palabras:
    abecedario=['e','a','o','s','r','n','i','d','l','c','t','u','m','p','b','g','v','y','q','h','f','z','j','ñ','x','k','w']
    
    huecos=len(palabra)
    intentos=0
    while huecos>0:

        for letraabc in abecedario:
            veces = palabra.count(letraabc)
            if veces>=1:               
                huecos-=veces
                intentos+=1
                abecedario.remove(letraabc)
                break
            else:
                abecedario.remove(letraabc)
                intentos+=1
                break  
    totalintentos+=intentos 

print(totalintentos)
                

                
                
         
  

 