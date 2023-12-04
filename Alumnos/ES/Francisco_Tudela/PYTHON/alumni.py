import random
from faker import Faker
from funciones import *
import json

def guardar_alumnos(lista_alumnos):
    with open('alumnos.json', 'w') as archivo:
        json.dump(lista_alumnos, archivo)

def cargar_alumnos():
    try:
        with open('alumnos.json', 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []

faker = Faker(['es-ES'])
alumnos = []

for data in range(20):
    alumno = {
        'NIF': faker.nif(),
        'Nombre': faker.first_name(),
        'Apellidos': faker.last_name(),
        'Teléfono': faker.phone_number(),
        'Email': faker.email(),
        'Aprobado': random.choice([True, False])
    }
    alumnos.append(alumno)

for i, alumno in enumerate(alumnos, start=1):
    print(f'Alumno {i}: {alumno}')

opcion_elegida = ''
while (opcion_elegida != 'X'):
    opcion_elegida = input('''
    Hola, escoge una opción:
    1 Añadir un alumno 
    2 Eliminar alumno por NIF
    3 Actualizar datos de un alumno por NIF
    4 Mostrar datos de un alumno por NIF
    5 Mostrar datos de un alumno por Email
    6 Listar TODOS os alumnos
    7 Aprobar Alumno por NIF
    8 Suspender Alumno por NIF
    9 Mostrar alumnos aprobados
    10 Mostrar alumnos suspensos
    X Finalizar Programa
    ''')
    if (opcion_elegida == '1'):
        add_alumni()
    elif (opcion_elegida == '2'):
        remove_alumni()
    elif (opcion_elegida == '3'):
        actualizar_data()
    elif (opcion_elegida == '4'):
    elif (opcion_elegida == '5'):
    elif (opcion_elegida == '6'):
    elif (opcion_elegida == '7'):
    elif (opcion_elegida == '8'):
    elif (opcion_elegida == '9'):
    elif (opcion_elegida == '10'):
    
        

        



