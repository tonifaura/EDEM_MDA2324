
#Ejercicios de comandos en la consola de linux.

  1.Listar todos los archivos del directorio bin.
  
  ls ./bin
     
  2.Listar todos los archivos del directorio tmp.
  
  ls ./tmp
    
  3.Listar todos los archivos del directorio etc que empiecen por t 
  
  cd ..
    ls -l t*
    
  4.Listar todos los archivos del directorio dev que empiecen por tty.
  
  ls /dev/tty*
    
  5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
  
  ls /dev/tty*3
    
    
  6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
  
  ls /dev/t*C1
    

  7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
  
  ls -la
    
    
  8.Listar todos los archivos del directorio etc que no empiecen por t.
  
  cd etc
    ls [!t]*
    
  9.Listar todos los archivos del directorio usr y sus subdirectorios.
  
  ls -R /usr
    

  10.Cambiarse al directorio tmp, crear directorio PRUEBA.
  
  cd /tmp
  mkdir PRUEBA
    

  11.Verificar que el directorio actual ha cambiado.
  
  pwd 
    

  12.Mostrar el día y la hora actual.
  
  date 
    

  13.Con un solo comando posicionarse en el directorio $HOME.
  
   cd ~
    
 
  14.Verificar que se está en él.
  
  pwd
    

  15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
  
  ls -l 
    

  16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.

    cd tmp
    cd prueba
    rm -r *

  17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio 
  dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
    
    mkdir dir1 dir2 dir3
    cd dir1
    mkdir dir11
    cd ..
    cd dir3
    mkdir dir31
    cd dir31
    mkdir dir311 dir312
    
  18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
    
    cd ../..
    touch mensaje
    cp /ect/motd mensaje

  19.Copiar mensaje en dir1, dir2 y dir3.
    
    cp mensaje dir1
    cp mensaje dir2
    cp mensaje dir3
    
  20.Comprobar el ejercicio anterior mediante un solo comando.
    
    ls -R
    