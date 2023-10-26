#Proyecto Final - Curso Python - EDEM_MDA2324

#Una empresa de formación quiere gestionar su cartera de alumnos.

#Escribe un programa que guarde una lista de alumnos. Cada Alumno dispone de los siguientes campos:

Clientes = [
    { 'NIF':'113004000R', 'nombre': 'Adriana', 'Apellidos': 'Campos Romero', 'Telefono': 69809977, 'Email':'adriana@gmail.com','Preferente':False},
    { 'NIF':'123004000R', 'nombre': 'Laura', 'Apellidos': 'Gonzalez Romero', 'Telefono': 69809977, 'Email':'laura@gmail.com','Preferente':False},
    { 'NIF':'133004000R', 'nombre': 'Paula', 'Apellidos': 'Alonso Romero', 'Telefono': 69809977, 'Email':'paula@gmail.com','Preferente':True},
    { 'NIF':'143004000R', 'nombre': 'Lucia', 'Apellidos': 'Vera Romero', 'Telefono': 69809977, 'Email':'lucia@gmail.com','Preferente':False}
]

print (Clientes)

print (Clientes[0]['NIF'])

#NIF (string)
#Nombre (string)
#Apellidos (string)
#Teléfono (string)
#Email (string)
#Aprobado (boolean)
#El programa debe mostrar las siguientes opciones por consola para que escoja el usuario:


opcion= int(input (' \n(1) Añadir un cliente \n(2) Eliminar cliente por NIF \n(3) Mostrar Cliente por NIF \n(4) Listar TODOS os clientes \n(5) Mostrar ÚNICAMENTE los clientes preferentes \n(6) Finalizar Programa \nElije una de estas opciones: '))

if opcion == 1:
  AddClient =     { 'NIF':'113004000R', 'nombre': 'Adriana', 'Apellidos': 'Campos Romero', 'Telefono': 69809977, 'Email':'adriana@gmail.com','Preferente':False
                  }
  Clientes.append(AddClient)
elif opcion == 2:
  EliminarCliente= input('Dime el NIF del cliente que quieres eliminar')
  Clientes.pop()
elif  opcion == 3:
  MostrarCliente= input('Dime el NIF del cliente que quieres mostrar')
  print()
elif  opcion == 4:
  print(Clientes)
elif  opcion == 5:
  for n in Clientes:
    if Clientes[n]['NIF']==True:
      print()
else:
  print ('FIN')



#(1) Añadir un alumno --> Esto activará una serie de preguntas para completar el nuevo alumno

#(2) Eliminar alumno por NIF

#(3) Actualizar datos de un alumno por NIF

#(4) Mostrar datos de un alumno por NIF

#(5) Mostrar datos de un alumno por Email

#(6) Listar TODOS os alumnos

#(7) Aprobar Alumno por NIF

#(8) Suspender Alumno por NIF

#(9) Mostrar alumnos aprobados

#(10) Mostrar alumnos suspensos

#(X) Finalizar Programa --> Únicamente se cierra el programa si el usuario pulsa la X