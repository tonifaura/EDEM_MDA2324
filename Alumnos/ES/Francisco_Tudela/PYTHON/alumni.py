from funciones import *

alumnos  = []
cargar_alumnos(alumnos)
guardar_alumnos(alumnos)
opcion_elegida = ''
while (opcion_elegida != 'X'):
    opcion_elegida = input('''
    Hola, escoge una opción:
    1 Añadir un alumno 
    2 Eliminar alumno por NIF
    3 Actualizar datos de un alumno por NIF
    4 Mostrar datos de un alumno por NIF
    5 Mostrar datos de un alumno por Email
    6 Listar TODOS os alumnos
    7 Aprobar Alumno por NIF
    8 Suspender Alumno por NIF
    9 Mostrar alumnos aprobados
    10 Mostrar alumnos suspensos
    X Finalizar Programa
    ''')
    if (opcion_elegida == '1'):
        add_alumni()
    elif (opcion_elegida == '2'):
        remove_alumni()
    elif (opcion_elegida == '3'):
        actualizar_data()
    elif (opcion_elegida == '4'):
        mostrar_data_alumni()
    elif (opcion_elegida == '5'):
        mostrar_datos_por_mail()
    elif (opcion_elegida == '6'):
        mostrar_total_alumnos()
    elif (opcion_elegida == '7'):
        aprobar_alumno()
    elif (opcion_elegida == '8'):
        suspender_alumno()
    elif (opcion_elegida == '9'):
        mostrar_alumnos_aprobados()
    elif (opcion_elegida == '10'):
        mostrar_alumnos_suspendidos()
        break
        

        



