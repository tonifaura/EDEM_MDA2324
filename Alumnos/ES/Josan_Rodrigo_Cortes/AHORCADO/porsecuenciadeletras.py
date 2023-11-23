
palabras=["Cosquillas", "Japonesa", "Aullar", "Amistad", "Matrimonio","Obligatorio", "Trenza", "Aldea", "Peinado", "Principal"]


totalintentos=0
for palabra in palabras:
    letras=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","y","z"]
    
    huecos=len(palabra)

    veces = palabra.count(letras)

    huecos-=veces

    letras.remove(letras)
                
                # veces = palabras.count(letraAzar)
    for letra in palabra:

        for l in letras:

            if l==letra:

               

        # huecos-=veces

        # letras.remove(letraAzar)

        intentos+=1
    totalintentos+=intentos
    print(intentos)
    print("Palabra acertada")


