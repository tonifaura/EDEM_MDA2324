""" (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
(2) Eliminar alumno por NIF
(3) Actualizar datos de un alumno por NIF
(4) Mostrar datos de un alumno por NIF
(5) Mostrar datos de un alumno por Email
(6) Listar TODOS os alumnos
(7) Aprobar Alumno por NIF
(8) Suspender Alumno por NIF
(9) Mostrar alumnos aprobados
(10) Mostrar alumnos suspensos
(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X """


from functions import *
#from alumnos import alumnos

alumnos=[]
funcion=" "
while funcion != "X": # or funcion!="x":
    print(alumnos)
    funcion=queOpcion()

    # (1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno
    if funcion=="1":
        anyadirAlumno()
        funcion=queOpcion()

    # (2) Eliminar alumno por NIF        
    if funcion=="2":
        eliminarAlumno()
        funcion=queOpcion()

            
"""   # (3) Actualizar datos de un alumno por NIF
    if funcion==3:
        funcion=3
        print(funcion)
        #def actualizarDatosAlumnoPorNIF():
            
    # (4) Mostrar datos de un alumno por nombre
    if funcion==4:
        funcion=4
        print(funcion)
        #def mostrarDatosAlumnoPorNombre():
                
    # (5) Mostrar datos de un alumno por Email
    if funcion==5:
        funcion=5
        print(funcion)
        #def mostrarDatosAlumnoPorEmail():
            
    # (6) Listar TODOS los alumnos
    if funcion==6:
        funcion=6
        print(funcion)
        #def mostrarDatosTodosAlumnos():
            
    # (7) Aprobar Alumno por NIF
    if funcion==7:
        funcion=7
        print(funcion)
        #def aprobarAlumnoPorNif():
            
    # (8) Suspender Alumno por NIF
    if funcion==8:
        funcion=8
        print(funcion)
        #def suspenderAlumnoPorNif():
            
    # (9) Mostrar alumnos aprobados
    if funcion==9:
        funcion=9
        print(funcion)
        #def mostrarAlumnosAprobados():
            
    # (10) Mostrar alumnos suspensos
    if funcion==10:
        funcion=10
        print(fun)
        #def mostarAlumnosSuspensos():
            
    # (X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X  """
print(alumnos)