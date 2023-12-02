#from alumnos import alumnos
alumnos=[]
def queOpcion():
        opcion=input("""
        BIENVENIDO A LA BASE DE DATOS DE ALUMNOS, QUE DESEA HACER, MARQUE LA OPCIÓN ELEGIDA:
        (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
        (2) Eliminar alumno por NIF
        (3) Actualizar datos de un alumno por NIF
        (4) Mostrar datos de un alumno por NIF
        (5) Mostrar datos de un alumno por Email
        (6) Listar TODOS os alumnos
        (7) Aprobar Alumno por NIF
        (8) Suspender Alumno por NIF
        (9) Mostrar alumnos aprobados
        (10) Mostrar alumnos suspensos
        (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X:  """
        )
        return opcion
#(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno

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
anyadirAlumno()
# anyadirAlumno()
print(alumnos)

# (2) Eliminar alumno por NIF        

def eliminarAlumno():
    nif=input("Introduce el NIF del alumno a elminar; ")
    for alumno in alumnos:
         if alumno["NIF"]==nif:
              alumnos.remove(alumno)

# eliminarAlumno()
# print(alumnos)
# (3) Actualizar datos de un alumno por NIF
def actualizarDatosAlumnoPorNIF():
    nif=input("Introduce el NIF del alumno a actualizar; ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            alumno["Nombre"]=input("Introduce el nombre a actualizar: ")
            alumno["Apellido1"]=input("Introduce el primer apellido a actualizar: ")
            alumno["Apellido2"]=input("Introduce el  segundo apellido actualizar: ")
    return

# actualizarDatosAlumnoPorNIF()
# print(alumnos)
# (4) Mostrar datos de un alumno por nombre
def mostrarDatosAlumnoPorNombre():
    nombre=input("Introduce el nombre del alumno a mostrar; ")
    for alumno in alumnos:
         if nombre==alumno:
            print(f"""
                    Estos son los datos del alumno seleccionado:
                    Nombre: {alumno["Nombre"]}, 
                    Primer apellido: {alumno["Apellido1"]}, 
                    Segundo apellido: {alumno["Apellido2"]},
                    y NIF: {alumno["NIF"]}.
                    """)

mostrarDatosAlumnoPorNombre()
print(alumnos)    
# (5) Mostrar datos de un alumno por Email

    #def mostrarDatosAlumnoPorEmail():
        
# (6) Listar TODOS los alumnos

    #def mostrarDatosTodosAlumnos():
        
# (7) Aprobar Alumno por NIF

    #def aprobarAlumnoPorNif():
        
# (8) Suspender Alumno por NIF

    #def suspenderAlumnoPorNif():
        
# (9) Mostrar alumnos aprobados

    #def mostrarAlumnosAprobados():
        
# (10) Mostrar alumnos suspensos
    #def mostarAlumnosSuspensos():
        
# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X """