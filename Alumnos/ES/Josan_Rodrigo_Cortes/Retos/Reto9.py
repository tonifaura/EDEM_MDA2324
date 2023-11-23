""" Reto 9
Escribe un programa que pueda decirte si un año (número entero) es bisiesto o no """


# print("AÑO BISIESTO??")
# anyo=int(input("Introduce el año a comprobar: "))
def anyoBisiesto(anyo):

    if anyo%4==0:
        print(f"El {anyo} es bisiesto")

    elif anyo%4==0 and anyo%100!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%4==0 and anyo%100!=0 and anyo%400!=0:
        print(f"El año {anyo} no es bisiesto")

    elif anyo%4==0 and anyo%100!=0 and anyo%400==0:
        print(f"El año {anyo} es bisiesto")

anyoBisiesto(3000)
# def añoBisiesto(anyyo):
#     if anyyo%4 and anyyo%100 and anyyo%400==0:
#         print("Bisiesto")
#     else:
#         print("No bisiesto")
    
# añoBisiesto(3000)