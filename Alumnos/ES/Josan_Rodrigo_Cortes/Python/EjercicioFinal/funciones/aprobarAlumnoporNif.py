# (7) Aprobar Alumno por NIF
from alumnos import alumnos

def aprobarAlumnoPorNif():
    nif=input("Introduce el NIF del alumno que deseas aprobar: ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            aprobado=input("Esta aprobado el alumno: (Si/No)")
            if aprobado=="Si":
                alumno["Calificacion"]="Aprobado"
            else:
               alumno["Calificacion"]="Suspendido" 

aprobarAlumnoPorNif()
print(alumnos)