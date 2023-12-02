# (2) Eliminar alumno por NIF        
from alumnos import alumnos
def eliminarAlumno():
    nif=input("Introduce el NIF del alumno a elminar; ")
    for alumno in alumnos:
         if alumno["NIF"]==nif:
              alumnos.remove(alumno)