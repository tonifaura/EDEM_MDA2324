palabras=["cosquillas"]
totalIntentos=0
letrasInpalabra=[]
intentos=0
for palabra in palabras:
    abecedario=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    huecos=len(palabra)
    
    for i in range(huecos):
        letrasInpalabra.append(" ")
    for letra in palabra:
        for letraabc in abecedario:
            veces=palabra.count()
            if letraabc is palabra:

                # for letra in palabra:#quito el hueco de la palabra y añado la letra
                # letrasInpalabra.remove(" ")
                # letrasInpalabra.append(letra)
                intentos+=1
                break
            else:
                intentos+=1
        


print(letrasInpalabra)
print(intentos)        
            