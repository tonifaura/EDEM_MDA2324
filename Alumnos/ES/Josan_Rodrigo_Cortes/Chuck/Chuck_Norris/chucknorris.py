import requests

print("Hello world")

file = open("~/Chuck_Norris2/Results/results.txt","a")

url = "https://api.chucknorris.io/jokes/random"

with open("results.txt", "a") as f:

    for i in range(5):

        #crea una solicitud para la api
        response = requests.get(url)
        #accede al json (diccionario) valor: "value (diccionario)"
        joke = response.json()["value"]
        #escribe el chiste en el .txt
        f.write(joke +" ")