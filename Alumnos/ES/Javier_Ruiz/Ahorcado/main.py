import pandas as pd
import time

# Lee el CSV
df = pd.read_csv('palabras.csv')

# Extrae la columna "Palabras" como una lista
palabras_lista = df['PALABRAS'].tolist()
palabras_lista = [palabra.lower() for palabra in palabras_lista] #las pongo en minuscula porque sino da problemas

# Ahorcado
letras_disponibles =  ['e', 'a', 'o', 'i', 's', 'r', 'n', 'l', 'u', 'd', 't', 'c', 'm', 'p', 'b', 'g', 'v', 'y', 'q', 'h', 'f', 'z', 'j', 'x', 'k', 'w']
total_intentos = 0
iniciocrono = time.time()

while palabras_lista:
    intentos_realizados = 0
    letras_correctas = 0

    palabra_seleccionada = palabras_lista[0]
    palabras_lista.remove(palabra_seleccionada)

    print(f'Palabra: {palabra_seleccionada}')

    numero_letras = len(palabra_seleccionada)

    for letra in letras_disponibles:
        intentos_realizados += 1     #suma 1 intento por cada letra intentada del set de letras disponible
        if palabra_seleccionada.count(letra) > 0:           #si la letra intentada esta presente en la palabra seleccionada
            letras_correctas += palabra_seleccionada.count(letra)         #aumenta el conteo de letras correctas segun las veces que aparezca
        if letras_correctas == numero_letras:
            break


    print(f'Numero de intentos : {intentos_realizados}')
    total_intentos += intentos_realizados

fincrono = time.time()
tiempo_transcurrido = fincrono - iniciocrono


print(f'Total de intentos: {total_intentos}')
print(f'Tiempo transcurrido: {round(tiempo_transcurrido, 2)} segundos')
