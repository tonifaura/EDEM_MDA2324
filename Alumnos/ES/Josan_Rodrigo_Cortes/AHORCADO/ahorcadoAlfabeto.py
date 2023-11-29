# Abecedario en el orden normal

palabras=["cosquillas", "japonesa", "aullar", "amistad", "matrimonio","obligatorio", "trenza", "aldea", "peinado", "principal"]
totalintentos=0

for palabra in palabras:
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    huecos=len(palabra)
    intentos=0
    while huecos>0:
        """     alabradescompuesta=[]
        for letras in palabra:
            palabradescompuesta.append(letras)
        palabradescompuesta.sort()
        palabraordenada="".join(palabradescompuesta) 
        """
       
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
                

                
                
         
  

 