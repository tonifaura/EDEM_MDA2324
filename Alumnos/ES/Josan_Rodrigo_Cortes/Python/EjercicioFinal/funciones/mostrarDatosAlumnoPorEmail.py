# (5) Mostrar datos de un alumno por Email
# from alumnos import alumnos
from alumnos import alumnos

def mostrarDatosAlumnoPorEmail():
    email=input("Introduce el email del alumno a mostrar: ")
    for alumno in alumnos:
        if email==alumno["Email"]:
            print(f"""
                    Estos son los datos del alumno seleccionado por email:
                    Nombre: {alumno["Nombre"]}, 
                    Primer apellido: {alumno["Apellido1"]}, 
                    Segundo apellido: {alumno["Apellido2"]},
                    y NIF: {alumno["NIF"]}. 
                    """)       
            
mostrarDatosAlumnoPorEmail()
            
