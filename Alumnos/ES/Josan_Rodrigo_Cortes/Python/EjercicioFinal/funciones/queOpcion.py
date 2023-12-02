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