""" Ejercicio 1
A partir de las respuestas a los dos últimos ejercicios de la Sesión 3:"""
# 1.Crea una función que reciba un rango de números como parámetro y muestre por consola 
# únicamente los valores primos

# Version 1
""" def primos(numero):
    if numero==0 or numero==1 or numero==4:
        return False
    else:
        for i in range(2,numero):
            if numero%i==0:
                return False
            else:
                return True

numerosPrimos=[]            
for i in range(5):
    
    numero=int(input("Introduce un numero: "))
    if primos(numero)==True:
        numerosPrimos.append(numero)
print(numerosPrimos) """

# Version 2

def primos2(numero=[]):
    numerosPrimos2=[]
    for numero in numerosPrimos2:

        if numero!=0 or numero!=1 or numero!=4:
            for i in range(2,numero):
                if numero%i!=0:
                    numerosPrimos2.append(i)
                    return numerosPrimos2
               
listanumeros=[]
for i in range (5):
    numero2=int(input("Introduce un numero: "))
    numero2.append(listanumeros)

print(primos2(listanumeros))
        
    

# 2.Crea una función que pueda evaluar si un número (pasado por parámetro) es primo o no
# 3.Crea una función que reciba un año y pueda indicarte con True o False si es un año bisiesto o no. 