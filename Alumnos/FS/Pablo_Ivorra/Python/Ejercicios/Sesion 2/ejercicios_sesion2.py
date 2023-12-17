#Crea una aplicación de consola que calcule los resultados de una inversión. Debe
#1.Pedir por consola una cantidad (numérica) de Inversión
#2.Pedir el % de interés anual
#3.Pedir el número de años que se va a mantener la inversión
#4.Finalmente, calcular la cantidad generada en los años especificados por el usuario

print("Bienvenido al sistema de cálculo de inversiones.")
dinero = float(input("Cuanto dinero tienes para invertir (€)? "))
interes = float(input("Cual es el interés anual? \nEscribelo en decimal, ej 5% = 0.05. "))
ano = int(input("Cuantos años quieres mantener la inversión? "))
profit = dinero*interes*ano

print(f"En {ano} años tendrás {profit}€ de interés")