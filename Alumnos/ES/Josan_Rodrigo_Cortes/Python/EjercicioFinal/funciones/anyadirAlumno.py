#(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
from alumnos import alumnos
def anyadirAlumno(funcion=1):
    nuevoAlumno={}
    nuevoAlumnoNombre=input("Introduce el nombre del nuevo alumno: ")
    nuevoAlumnoApellido1=input("Introduce el primer apellido del alumno: ")
    nuevoAlumnoApellido2=input("Introduce el segundo apellido del alumno: ")
    nuevoAlumnoNIF=input("Introduce el NIF del alumno")

    nuevoAlumno.setdefault("Nombre"," ")
    nuevoAlumno.setdefault("Apellido1", " ")
    nuevoAlumno.setdefault("Apellido2"," ")
    nuevoAlumno.setdefault("NIF"," ")

    nuevoAlumno["Nombre"]=nuevoAlumnoNombre
    nuevoAlumno["Apellido1"]=nuevoAlumnoApellido1    
    nuevoAlumno["Apellido2"]=nuevoAlumnoApellido2
    nuevoAlumno["NIF"]=nuevoAlumnoNIF
    alumnos.append(nuevoAlumno)
    return