""" Escribe una función que calcule el área de un triángulo, recibiendo la altura 
y la base como parámetros y otra función que calcule el área de un círculo
recibiendo el radio del mismo. """

base=int(input("Introduce la base del triangulo"))
altura=int(input("Introduce la altura del triangulo"))

def areaTriangulo(b,a):
    areat=(b*a)/2
    print(areat)
    
areaTriangulo(base,altura)

phi=3.14

def areaCirculo(r):
    areaCirculo=phi*r**2
