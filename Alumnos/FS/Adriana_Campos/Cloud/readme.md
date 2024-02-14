# Caso de uso

Cada tienda de comestibles, que opera con sus propios procesos internos, proporcionará datos transaccionales que se almacenarán en nuestro almacenamiento de objetos. Por lo tanto, se requiere que los procesos internos de cada tienda de abarrotes cuenten con los permisos necesarios para ejecutar esta acción.

Implemente una arquitectura basada en eventos , asegurando que los datos se almacenen inmediatamente en las tablas respectivas. La solución debe optimizarse en términos de utilización de recursos y rentabilidad.

Dada la familiaridad de nuestro equipo de datos con Postgres como base de datos, es la opción preferida para este proyecto.

El panel final debe exponerse como un servicio para permitir el acceso a diferentes equipos.

# Person 1
# ejecutar

gcloud compute instances create "vm-test-1" \
    --image-project=debian-cloud \
    --image-family=debian-11 \
    --machine-type n1-standard-1 \
    --service-account=vm-endtoend@woven-justice-411714.iam.gserviceaccount.com \
    --scopes cloud-platform \
    --metadata-from-file=startup-script=./startup-script.sh


# Person 2
# ejecutar
