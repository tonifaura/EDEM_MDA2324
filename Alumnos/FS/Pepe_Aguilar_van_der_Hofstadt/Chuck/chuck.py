import requests
import pandas as pd

def random_chuck_norris_joke(url: str) -> str:

    respuesta = requests.get(url)
    estado: int = respuesta.status_code
    datos = respuesta.json()
    if estado == 200 and estado < 300:
        chuck_joke: str = datos['value']
        return(chuck_joke)
    else:
        print(f'error {estado}')
    
def separa_sustantivos(broma:str, todos_sustantivos) -> list:
    sustantivos = []
    broma_separada = broma.split()
    for palabra in broma_separada:
        for sust in todos_sustantivos:
            if(palabra.lower() == sust):
                sustantivos.append(palabra)
    return(sustantivos)

sust_veces = dict[]



sustantivos_df = pd.read_csv('nounlist.csv', header=None, names=['sustantivos'])
palabras = sustantivos_df['sustantivos'].str.strip('"').tolist()

URL:str = 'https://api.chucknorris.io/jokes/random'


broma = random_chuck_norris_joke(URL)
print(separa_sustantivos(broma, palabras))









