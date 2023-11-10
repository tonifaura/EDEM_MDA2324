print("Hola mundo")


import requests
import time

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

import requests
import time

url = 'https://api.chucknorris.io/jokes/random'
bromas = ""
try:
    while True:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            bromas = bromas+data['value']+"\n"
            print(bromas)
        else:
            print(f'Error en la solicitud. Código de estado: {response.status_code}')

        time.sleep(3)

except KeyboardInterrupt:
        print("¡Bucle interrumpido por el usuario!")

with open("results.txt", "a") as f:
    
    f.write(bromas+ "\n")