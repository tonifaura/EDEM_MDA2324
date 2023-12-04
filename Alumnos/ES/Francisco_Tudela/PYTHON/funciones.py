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
        del alumnos['NIF']
            
def actualizar_data():
    while True:
        nif_alumno = input('Indique el NIF del alumno con la letra al final:').upper()
        if len(nif_alumno) == 9 and nif_alumno[:8].isdigit():
            break
        else:
            print("Formato incorrecto. Asegúrese de ingresar 8 números seguidos de 1 letra.")
    if nif_alumno in alumnos: