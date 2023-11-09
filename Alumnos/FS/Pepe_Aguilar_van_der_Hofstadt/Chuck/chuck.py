import requests


def random_chuck_norris_joke(url: str) -> str:

    respuesta = requests.get(url)
    estado: int = respuesta.status_code
    datos = respuesta.json()
    if estado == 200 and estado < 300:
        chuck_joke: str = datos['value']
        return(chuck_joke)
    else:
        print(f'error {estado}')
    

URL:str = 'https://api.chucknorris.io/jokes/random'

print(random_chuck_norris_joke(URL))









