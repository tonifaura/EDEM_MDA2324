print("Hola mundo")

import requests
import time

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

if response.status_code == 200:

    data = response.json()
    print(data['value'])

else:
    print(f'Error en la solicitud. Código de estado: {response.status_code}')
try:
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(data['value'])
        else:
            print(f'Error en la solicitud. Código de estado: {response.status_code}')

        time.sleep(3)

except KeyboardInterrupt:
        print("¡Bucle interrumpido por el usuario!")