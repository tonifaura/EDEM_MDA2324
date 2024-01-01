def main():
    print(f'¿Qué quieres hacer?\n'
          f'1 --> Añadir alumno\n'
          f'2 --> Eliminar alumno por NIF\n'
          f'3 --> Actualizar datos de alumno por NIF\n'
          f'4 --> Mostrar datos de un alumno por NIF\n'
          f'5 --> Mostrar datos de un alumno por Email\n'
          f'6 --> Listar todos los alumnos\n'
          f'7 --> Aprobar alumno por NIF\n'
          f'8 --> Suspender alumno por NIF\n'
          f'9 --> Mostrar alumnos aprobados\n'
          f'10 --> Mostrar alumnos suspensos\n'
          f'X --> Salir')

    numero = input('')

    alumnos = []

    Alumno = {
        "NIF": 'Viva el Pop',
        "Nombre": 'Taylor Swift',
        "Apellidos": 2012,
        "Teléfono": 42,
        "Email": 'Pop',
        "Aprobado": 'Pop'
    }

    if (numero == '1'):
        añadir_alumno()
    
    #elif (numero == '2'): 
    #    eliminar_alumno()   
    #
    #elif (numero == '3'):  
    #    actualizar_datos()
    #        
    #elif (numero == '4'):
    #    mostrar_por_nif()
    #
    #elif (numero == '5'):
    #    mostrar_por_email()
    #
    #elif (numero == '6'):
    #    listar_todos()
    #
    #elif (numero == '7'):
    #    aprobar_alumno()
    #    
    #elif (numero == '8'):
    #    suspender_alumno()
    #    
    #elif (numero == '9'):
    #    mostrar_aprobados()
    #    
    #elif (numero == '10'):
    #    mostrar_suspensos()
    
    elif (numero.upper() == 'X'):
        salir()
            
    else:
        print(f'Caracter no válido. Proporciona otro.')
        main()

def añadir_alumno():
    print(f'Prueba')

def salir():
    print(f'¡Nos vemos!')
    exit()
    
main()