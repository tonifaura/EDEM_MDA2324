# Linux_Comandos

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.


Ejercicio de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
    
     ls /bin 
    
  2.Listar todos los archivos del directorio tmp.
   
    ls /tmp
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
    
    ls /etc/t*
  
  4.Listar todos los archivos del directorio dev que empiecen por tty.
    
    ls /dev/tty*
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
    
    ls /dev/tty*3   
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
    
    ls /dev/t*c1
    

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
    
    ls -a/
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
    
    ls -d /etc/[^t]*

  9.Listar todos los archivos del directorio usr y sus subdirectorios.
    
    ls -R/usr

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
    
    cd /tmp
    mkdir PRUEBA

  11.Verificar que el directorio actual ha cambiado.
    
    pwd

  12.Mostrar el día y la hora actual.
    
    date

  13.Con un solo comando posicionarse en el directorio $HOME.
    
    cd /HOME
 
  14.Verificar que se está en él.
    
    pwd

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
    
    ls -l HOME

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
    
    rm-r PRUEBA

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    echo "volvemos al directorio PRUEBA"
    cd PRUEBA 
    echo "desde directorio PRUEBA, creamos dir1, dir2 y dir3" 
    mkdir dir1 dir2 dir 3
    echo "vamos a dir1 y creamos dir11"
    cd dir1
    mkdir dir11  
    echo "volvemos al directorio PRUEBA"
    cd ..
    echo "vamos a dir3 y creamos dir31"
    cd dir3
    mkdir dir31
    echo "nos aseguramos de que estamos dentro de dir31"
    cd dir31
    echo "dentro del dir31, creamos dir311 y dir312"
    mkdir dir311 dir312

 
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    cp etc/motd PRUEBA/mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    cp PRUEBA/mensaje PRUEBA/dir1/
    cp PRUEBA/mensaje PRUEBA/dir2/
    cp PRUEBA/mensaje PRUEBA/dir3/

    
  20.Comprobar el ejercicio anterior mediante un solo comando.
  
  
  ls PRUEBA/dir1 PRUEBA/dir2 PRUEBA/dir3
