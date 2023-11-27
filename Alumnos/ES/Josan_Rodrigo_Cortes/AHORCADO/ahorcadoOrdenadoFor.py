
#palabras=["Cosquillas", "Japonesa", "Aullar", "Amistad", "Matrimonio","Obligatorio", "Trenza", "Aldea", "Peinado", "Principal"]

#FALTA REVISAR LA VARIABLE CONTADOR PORQUE NO ME CUADRA EL NUMERO QUE ME DA, 
# REVISAR TAMBIEN EL ULTIMO IF
#Mayúsculas a minusculas
# palabras=["aabbcd","aullar","obligatorio"]
palabras=["cosquillas"]
intentos=0

for palabra in palabras:
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    huecos=len(palabra)
    listaletraRepetidas=[]  
    totalintentos=0
    # while huecos>0:       
    vecesLetraenPalabra=0
    intentosletra=0
    for letra in palabra:
        for cadaLetra in abecedario:
            veces = palabra.count(palabra)
            
            if cadaLetra==letra:
                if veces-vecesLetraenPalabra>1:
                    listaletraRepetidas.append(letra)
                    huecos-=1
                    vecesLetraenPalabra+=1
                    break
                else:
                    intentosletra+=1
                    break
                            
            else:
              intentosletra+=1
        totalintentos+=intentosletra  
  
print(totalintentos)
