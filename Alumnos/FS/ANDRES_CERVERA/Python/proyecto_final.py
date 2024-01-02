alumnos = []

#llamado de funciones desde main
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
          f'10 --> Mostrar alumnos suspendidos\n'
          f'X --> Salir')

    numero = input('')

    if (numero == '1'):
        añadir_alumno()
    
    elif (numero == '2'): 
        eliminar_alumno()   
    
    elif (numero == '3'):  
        actualizar_datos()
           
    elif (numero == '4'):
        mostrar_por_nif()
    
    elif (numero == '5'):
        mostrar_por_email()
    
    elif (numero == '6'):
       listar_todos()
    
    elif (numero == '7'):
       aprobar_alumno()
       
    elif (numero == '8'):
        suspender_alumno()
        
    elif (numero == '9'):
        mostrar_aprobados()
        
    elif (numero == '10'):
        mostrar_suspendidos()
    
    elif (numero.upper() == 'X'):
        salir()
            
    else:
        print(f'Caracter no válido. Proporciona otro.')
        main()

#funcion añadir alumno
def añadir_alumno():
    print(f'Rellene los siguientes datos:\n')
    NIF = input('NIF: ')
    Nombre = input('Nombre: ')
    Apellidos = input('Apellidos: ')
    Telefono = input('Telefono: ')
    Email = input('Email: ')
    Calificacion = 'NC'
    
    nuevo_alumno = {
            "NIF": NIF,
            "Nombre": Nombre,
            "Apellidos": Apellidos,
            "Telefono": Telefono,
            "Email": Email,
            "Calificacion": Calificacion
        }
    
    alumnos.append(nuevo_alumno)
    print(f'Alumno añadido correctamente.')
    main()

def eliminar_alumno():
    print(f'Escriba el NIF del alumno a eliminar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumnos.remove(alumno) 
            print(f'Alumno eliminado correctamente')  
    print(f'No se ha encontrado ningún alumno con ese NIF')
    otra_operacion()
    
def actualizar_datos():
    print(f'Escriba el NIF del alumno a actualizar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(alumno['NIF'] == NIF):
            print(f'{alumno}\n')
            
def mostrar_por_nif():
    print(f'Escriba el NIF del alumno a mostrar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(alumno['NIF'] == NIF):
            print(f'{alumno}\n')
            
def mostrar_por_email():
    print(f'Escriba el Email del alumno a mostrar:\n')
    email = input('Email: ')
    for alumno in alumnos:
        if(alumno['Email'] == email):
            print(f'{alumno}\n')
            
def aprobar_alumno():
    print(f'Escriba el NIF del alumno a aprobar:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumno['Calificacion'] = 'Aprobado'   
            return

def suspender_alumno():
    print(f'Escriba el NIF del alumno a suspender:\n')
    NIF = input('NIF: ')
    for alumno in alumnos:
        if(NIF == alumno['NIF']):
            alumno['Calificacion'] = 'Suspendido'   
            return

def mostrar_aprobados():
    for alumno in alumnos:
        if(alumno['Calificacion'] == 'Aprobado'):
            print(f'{alumno}\n')

def mostrar_suspendidos():
    for alumno in alumnos:
        if(alumno['Calificacion'] == 'Suspendido'):
            print(f'{alumno}\n')
                   
#funcion listar alumno
def listar_todos():
    for alumno in alumnos:
        print(f'Alumno {alumno}: {alumnos}\n')
    otra_operacion()

def otra_operacion():
    print(f'¿Desea realizar otra operación?\n'
          f'1 --> Sí\n'
          f'X -- Salir')
    numero = input('')
    if (numero == 1):
        main()
    elif (numero.upper() == 'X'):
        salir()
    else:
        print(f'Caracter no válido')
        otra_operacion()

def salir():
    print(f'¡Nos vemos!')
    exit()

 #llamada al programa 
main()