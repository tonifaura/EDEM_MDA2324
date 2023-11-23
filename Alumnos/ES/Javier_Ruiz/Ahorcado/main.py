import pandas as pd
import numpy as np
import time

class Ahorcado:
    def __init__(self, palabra):
        self.palabra = palabra
        self.letras_adivinadas = set()

    def mostrar_palabra(self):
        return ''.join([letra if letra in self.letras_adivinadas else '_' for letra in self.palabra])

    def adivinar(self, letra):
        self.letras_adivinadas.add(letra)
        return letra in self.palabra

    def juego_terminado(self):
        return set(self.palabra) == self.letras_adivinadas


def jugar_ahorcado_automatico(palabra):
    ahorcado = Ahorcado(palabra)
    intentos = 0

    while not ahorcado.juego_terminado():
        letra = np.random.choice([letra for letra in palabra if letra.isalpha()])
        
        if letra in ahorcado.letras_adivinadas:
            continue

        if ahorcado.adivinar(letra):
            pass  # Puedes imprimir mensajes si lo deseas, pero para automatizar, no es necesario.
        else:
            pass

        intentos += 1

    print(f"¡Felicidades! Has adivinado la palabra: {ahorcado.palabra}")
    print(f"Intentos realizados: {intentos}")

if __name__ == "__main__":
    try:
        palabras_df = pd.read_csv('palabras.csv')
        palabras = palabras_df['Palabra'].tolist()
    except FileNotFoundError:
        print("No se encontró el archivo 'palabras.csv'.")
        palabras = []

    if palabras:
        for palabra_seleccionada in palabras:
            print(f"Jugando con la palabra: {palabra_seleccionada}")
            jugar_ahorcado_automatico(palabra_seleccionada)
            print("------------------------------")
    else:
        print("No hay palabras disponibles para jugar.")
