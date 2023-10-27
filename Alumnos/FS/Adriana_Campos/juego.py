#Juego
#elegir palabras 

palabras =  ['hola' ,'manzana', 'sanwich' ]
print (palabras[1])

# Tiempo
# Intentos
intento = 0

for x in range(0,3):
   palabra = palabras[x]
   for i in palabra:
    letra = input("Escribe una letra:")
    if (letra in palabra):
        print('Has acertado')
    else:
        print('No has acertado')
        intento += intento