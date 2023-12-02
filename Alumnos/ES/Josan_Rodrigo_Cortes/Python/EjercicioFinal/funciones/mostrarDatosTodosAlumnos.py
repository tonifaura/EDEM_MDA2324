# (6) Listar TODOS los alumnos

from alumnos import alumnos

def mostrarDatosTodosAlumnos():
    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion!=" ":

            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación {calificacion}''')
        else:
            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación (pendiente de calificar)''')

        
        
mostrarDatosTodosAlumnos()