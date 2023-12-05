import json
import random
from faker import Faker

def generar_datos_fake(cantidad):
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
    
    for i, alumno in enumerate(alumnos, start=1): #No necesario, para ver datos por consola
        print(f'Alumno {i}: {alumno}')
    
    return alumnos  

def guardar_alumnos(alumnos, alumnos_json):
    with open('alumnos.json', 'w') as archivo:
        json.dump(alumnos, archivo,indent=2)

alumnos = generar_datos_fake(20)
guardar_alumnos(alumnos, 'alumnos.json')