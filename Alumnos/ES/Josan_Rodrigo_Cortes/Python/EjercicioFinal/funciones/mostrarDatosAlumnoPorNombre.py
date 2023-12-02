# (4) Mostrar datos de un alumno por nombre
from alumnos import alumnos
def mostrarDatosAlumnoPorNombre():
    nombre=input("Introduce el nombre del alumno a mostrar; ")
    for alumno in alumnos:
        
        if nombre==alumno["Nombre"]:

            print(f"""
                    Estos son los datos del alumno seleccionado por nombre:
                    Nombre: {alumno["Nombre"]}, 
                    Primer apellido: {alumno["Apellido1"]}, 
                    Segundo apellido: {alumno["Apellido2"]},
                    y NIF: {alumno["NIF"]}.
                    """)
            
