from alumnos import alumnos
# alumnos=[]
def queSubOpcion(subopcion=" "):
        subopcion=input("""
        Introduce el campo sobre el que ejecutar la acción elegida:
        (1) Nombre
        (2) Apellido1
        (3) Apellido2
        (4) Email
        (5) Calificacion
         """
        )
        if subopcion=="1":
            for alumno in alumnos:
                alumnoNombre=alumno["Nombre"]
                print(f"{alumnoNombre}")

        if subopcion=="2":
            for alumno in alumnos:
                alumnoApellido1=alumno["Apellido1"]
                print(f"{alumnoApellido1}")
        if subopcion=="3":
            for alumno in alumnos:
                alumnoApellido2=alumno["Apellido2"]
                print(f"{alumnoApellido2}")
        if subopcion=="4":
            for alumno in alumnos:
                alumnoEmail=alumno["Email"]
                print(f"{alumnoEmail}")
        if subopcion=="5":
            for alumno in alumnos:
                alumnoCalificacion=alumno["Calificacion"]
                print(f"{alumnoCalificacion}")
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
    nuevoAlumnoEmail=input("Introduce el email del alumno")

    nuevoAlumno.setdefault("Nombre"," ")
    nuevoAlumno.setdefault("Apellido1", " ")
    nuevoAlumno.setdefault("Apellido2"," ")
    nuevoAlumno.setdefault("NIF"," ")
    nuevoAlumno.setdefault("Email"," ")
    nuevoAlumno.setdefault("Calificacion"," ")

    nuevoAlumno["Nombre"]=nuevoAlumnoNombre
    nuevoAlumno["Apellido1"]=nuevoAlumnoApellido1    
    nuevoAlumno["Apellido2"]=nuevoAlumnoApellido2
    nuevoAlumno["NIF"]=nuevoAlumnoNIF
    nuevoAlumno["Email"]=nuevoAlumnoEmail
    alumnos.append(nuevoAlumno)
    return


# (2) Eliminar alumno por NIF        

def eliminarAlumno():
    mostrarDatosTodosAlumnos()
    nif=input("Introduce el NIF del alumno a elminar; ")
    for alumno in alumnos:
         if alumno["NIF"]==nif:
              alumnos.remove(alumno)


# (3) Actualizar datos de un alumno por NIF, preguntar el campo a actualizar!!!
def actualizarDatosAlumnoPorNIF():
    mostrarDatosTodosAlumnos()
    nif=input("Introduce el NIF del alumno a actualizar; ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            alumno["Nombre"]=input("Introduce el nombre a actualizar: ")
            alumno["Apellido1"]=input("Introduce el primer apellido a actualizar: ")
            alumno["Apellido2"]=input("Introduce el  segundo apellido actualizar: ")
            alumno["Email"]=input("Introduce el email actualizar: ")
    return

# actualizarDatosAlumnoPorNIF()
# print(alumnos)
# (4) Mostrar datos de un alumno por nombre
def mostrarDatosAlumnoPorNombre():
    mostrarDatosTodosAlumnos()
    nombre=input("Introduce el nombre del alumno a mostrar; ")
    for alumno in alumnos:
        nombre=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if nombre==alumno["Nombre"]:
            print(f"""
                        Estos son los datos del alumno seleccionado:
                        Nombre: {nombre},
                        Primer apellido: {apellido1}, 
                        Segundo apellido: {apellido2},
                        NIF: {nif},
                        Email: {email} y
                        Calificacion: {calificacion}
                        """)
   
# (5) Mostrar datos de un alumno por Email

def mostrarDatosAlumnoPorEmail():
    mostrarDatosTodosAlumnos()
    email=input("Introduce el email del alumno a mostrar: ")
    for alumno in alumnos:
        nombre=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if email==alumno["Email"]:
            print(f"""
                        Estos son los datos del alumno seleccionado:
                        Nombre: {nombre},
                        Primer apellido: {apellido1}, 
                        Segundo apellido: {apellido2},
                        NIF: {nif},
                        Email: {email} y
                        Calificacion: {calificacion}
                        """)
         
# (6) Listar TODOS los alumnos

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
            


# (7) Aprobar Alumno por NIF

def aprobarAlumnoPorNif():
    mostrarDatosTodosAlumnos()
    nif=input("Introduce el NIF del alumno que deseas aprobar: ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            aprobado=input("Esta aprobado el alumno: (Si/No)")
            if aprobado=="Si":
                alumno["Calificacion"]="Aprobado"
            else:
               alumno["Calificacion"]="Suspenso" 
        
# (8) Suspender Alumno por NIF

def suspenderAlumnoPorNif():
    mostrarDatosTodosAlumnos()
    nif=input("Introduce el NIF del alumno que deseas aprobar: ")
    for alumno in alumnos:
        if alumno["NIF"]==nif:
            aprobado=input("Esta aprobado el alumno: (Si/No)")
            if aprobado=="No":
                alumno["Calificacion"]="Aprobado"
            else:
               alumno["Calificacion"]="Suspenso" 
        
# (9) Mostrar alumnos aprobados

def mostrarAlumnosAprobados():

    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion=="Aprobado":

            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación {calificacion}''')
        
        
# (10) Mostrar alumnos suspensos
def mostrarAlumnosSuspensos():

    i=0
    for alumno in alumnos:
        i+=1
        nombreAlumno=alumno["Nombre"]
        apellido1=alumno["Apellido1"]
        apellido2=alumno["Apellido2"]
        nif=alumno["NIF"]
        email=alumno["Email"]
        calificacion=alumno["Calificacion"]
        if calificacion=="Suspenso":

            print(f'''
{i} {nombreAlumno} {apellido1} {apellido2}, NIF {nif}, {email} y calificación {calificacion}''')
        
# (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X """