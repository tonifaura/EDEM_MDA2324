import requests
import pandas as pd

class Sustantivo:
    palabra:str
    veces:int

    def __init__(self, _palabra):
        self.palabra = _palabra
        self.veces = 1
    
    def suma_vez(self):
        self.veces += 1

    def reset(self):
        self.veces = 0

lista_sustantivos = []

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
                if(len(lista_sustantivos) == 0):
                    sustantivo_nuevo = Sustantivo(palabra)
                    sustantivo_nuevo.reset()
                    lista_sustantivos.append(sustantivo_nuevo)
                for repetir in lista_sustantivos:
                    
                    if(repetir.palabra == palabra):
                        repetir.suma_vez()
                    else:
                        sustantivo_nuevo = Sustantivo(palabra)
                        lista_sustantivos.append(sustantivo_nuevo)
                #sustantivos.append(palabra)
    return(sustantivos)




sustantivos_df = pd.read_csv('nounlist.csv', header=None, names=['sustantivos'])
palabras = sustantivos_df['sustantivos'].str.strip('"').tolist()

URL:str = 'https://api.chucknorris.io/jokes/random'


broma = random_chuck_norris_joke(URL)
sustativos_chiste = separa_sustantivos(broma, palabras)

print(broma)
for palabras in lista_sustantivos:
    print(f'{palabras.palabra} {palabras.veces}')















