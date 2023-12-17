import requests


# obtenemos por el terminal lo que hay en la API

ret=requests.get("https://pokeapi.co/api/v2/pokemon/1")
print(ret)
print(ret.json())
