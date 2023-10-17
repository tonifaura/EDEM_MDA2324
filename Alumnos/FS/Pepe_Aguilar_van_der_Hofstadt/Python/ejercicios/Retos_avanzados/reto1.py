# RETO_1_av

# VENTA DE DISCOS.
# Venta de los discos almacenados en stock (en vez de diccionarios utilizaré POO)
# En vez de crear los discos uno a uno, haré un programa que los cree aleatoriamente.

# El programa debe dar a elegir al usuario que discos comprar y imprimir un ticket de compra
# Los discos de Black Metal y de Electro tienen 30% de descuento

import requests
import random
from datetime import date

URL:str = 'https://randomuser.me/api/'
NUM_DISCOS = 25
TODAY = date.today()
n_left = 1

class Disco:
    name: str
    artist: str
    year: int
    price: float
    genre: str
    permited_genre = ["Pop", "Electro", "Reggaeton", "Rock", "Metal", "Death Metal", "Black Metal"]

    def __init__(self, _name, _artist, _year, _price, _genre):
        self.name = _name
        self.artist = _artist
        self.year = _year
        self.price = _price

        if _genre in Disco.permited_genre:      # solo deja crear discos de los generos permitidos
            self.genre = _genre
        else:
            raise ValueError("El género no es válido. Debe ser Pop, Electro, Reggaeton, Rock, Metal, Death Metal, Black Metal")


def random_name(url: str) -> str:
    respuesta = requests.get(url)
    status_code = respuesta.status_code
    datos = respuesta.json()
    if(status_code == 200):
        clase = datos['results'][0]
        nombre: str = clase["name"]["first"]
        apellido: str = clase["name"]["last"]
        return(f"{nombre}_{apellido}")
    else:
        return(f"Error: {status_code}")

def disco_random(num:int) -> Disco:
    cd_name = f"random_cd_{num}"
    cd_artist = random_name(URL)
    cd_year = random.randint(1940, TODAY.year)
    cd_price = float(random.randint(12,35))-0.01
    permited_genre = ["Pop", "Electro", "Reggaeton", "Rock", "Metal", "Death Metal", "Black Metal"]
    cd_genre = random.choices(permited_genre, k=1)[0]
    return(Disco(cd_name, cd_artist, cd_year, cd_price, cd_genre))

cd1 = disco_random(1)
print(cd1.name)
print(cd1.artist)
print(cd1.year)
print(cd1.price)
print(cd1.genre)











