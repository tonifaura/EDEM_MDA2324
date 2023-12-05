import json
def cargar_alumnos():
    try:
        with open('alumnos.json', 'r') as file:
            alumnos = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        alumnos = []

def guardar_alumnos():
    with open('alumnos.json', 'w') as file:
        json.dump(alumnos, file, indent=2)

def add_alumni():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno not in alumnos:
        nuevo_alumno: {}
        nuevo_alumno['NIF'] = nif_alumno
        nuevo_alumno['Nombre'] = str(input('Indica el nombre del Alumno:'))
        nuevo_alumno['Apellidos'] = str(input('Indica el apellido del Alumno:'))
        nuevo_alumno['Teléfono'] = int(input('Indica el teléfono del Alumno:'))
        nuevo_alumno['Email'] = str(input('Indica el email del Alumno:'))
        nuevo_alumno['Aprobado'] = bool(input('Indica si el Alumno esta aprobado o suspendido:'))


def remove_alumni():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos:
        del alumnos[nif_alumno]['NIF']
            
def actualizar_data():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos:
         mod_nombre = input('Se modifica el nombre Y / N')
    if mod_nombre.upper() == 'Y':
        alumnos[nif_alumno]['Nombre'] = str(input('Indica el nombre del Alumno:'))
        mod_apellido = input('Se modifica el apellido Y / N')
    if mod_apellido.upper() == 'Y':
        alumnos[nif_alumno]['Apellidos'] = str(input('Indica el apellido del Alumno:'))
        mod_telefono = input('Se modifica el telefono Y / N')
    if mod_telefono.upper() == 'Y':
        alumnos[nif_alumno]['Teléfono'] = int(input('Indica el teléfono del Alumno:'))
        mod_email = input('Se modifica el mail Y / N')
    if mod_email.upper() == 'Y':
        alumnos[nif_alumno]['Email'] = str(input('Indica el email del Alumno:'))
        mod_nota = input('Se modifica la nota Y / N')
    if mod_nota.upper() == 'Y':
        alumnos[nif_alumno]['Aprobado'] = bool(input('Indica si el Alumno esta aprobado o suspendido:'))

def mostrar_data_alumni():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos:
        alumnos[nif_alumno]
        print(f'Datos del alumno con NIF {nif_alumno}:')

def mostrar_datos_por_mail():
    while True:
        mail_alumno = input('Indique el mail del alumno:')
        if mail_alumno in alumnos:
            alumnos[mail_alumno]
            print(f'Datos del alumno con NIF {mail_alumno}:')
            break
        else:
            print(f'No se encontró ningún alumno con el correo {mail_alumno}.')
            break

def mostrar_total_alumnos():
   for i, (alumno,apellido) in enumerate(alumnos.items(), start = 1):
       nombre = alumno['Nombre']
       apellido = alumno['Apellido']
       print(f'Alumno {i}: Nombre = {nombre}, Apellido = {apellido}')

def aprobar_alumno():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos:
        alumnos[nif_alumno]['Aprobado'] = True

def suspender_alumno():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos:
        alumnos[nif_alumno]['Aprobado'] = False

def mostrar_alumnos_aprobados():
      print('Alumnos Aprobados:')
for NIF, alumno in alumnos.items():
    if alumno['Aprobado'][True]:
        print(f"NIF: {NIF}, Nombre: {alumno['Nombre']}, Aprobado: {alumno['Aprobado']}")


def mostrar_alumnos_suspendidos():
    print('Alumnos Suspendidos:')
for NIF, alumno in alumnos.items():
    if alumno['Aprobado'][False]:
        print(f"NIF: {NIF}, Nombre: {alumno['Nombre']}, Aprobado: {alumno['Aprobado']}")
