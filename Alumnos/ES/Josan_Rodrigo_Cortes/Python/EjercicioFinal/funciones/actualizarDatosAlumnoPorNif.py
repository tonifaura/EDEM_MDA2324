# (3) Actualizar datos de un alumno por NIF
from alumnos import alumnos

def actualizarDatosAlumnoPorNIF():
    nif=input("Introduce el NIF del alumno a actualizar; ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            alumno["Nombre"]=input("Introduce el nombre a actualizar: ")
            alumno["Apellido1"]=input("Introduce el primer apellido a actualizar: ")
            alumno["Apellido2"]=input("Introduce el  segundo apellido actualizar: ")
    return