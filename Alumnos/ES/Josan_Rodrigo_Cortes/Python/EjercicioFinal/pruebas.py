alumnos=[
    {
        "Nombre":"Josan",
     "Apellido1":"Rodrigo",
     "Apellido2":"Cortes",
     "NIF":"1",
     "Email":"josan@email.com",
     "Calificacion":"Aprobado"
    },
    {
        "Nombre":"Laura",
     "Apellido1":"Jimenez",
     "Apellido2":"Ruiz",
     "NIF":"2",
     "Email":"laura@email.com",
     "Calificacion":"Aprobado"
    },
    {
        "Nombre":"Josan",
     "Apellido1":"Rodrigo",
     "Apellido2":"Jimenez",
     "NIF":"3",
     "Email":"josan2@email.com",
     "Calificacion":" "
    },
    {
        "Nombre":"Claudio",
     "Apellido1":"Rodrigo",
     "Apellido2":"Jimenez",
     "NIF":"4",
     "Email":"claudio@email.com",
     "Calificacion":" "
    }
    ]

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
            
mostrarAlumnosAprobados()