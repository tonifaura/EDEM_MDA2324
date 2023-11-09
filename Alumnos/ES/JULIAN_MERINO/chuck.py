# This is a python script that prints 'Hola mundo', connects to Chick Norris' API,
# processes the results and writes the output in 'results.txt'

# Print 'Hola mundo'
print(f'Hola mundo')

# Connect to Chuck Norri's API:
# installs the requests package to connect to the APIs
import requests
import json

# We create a function to request the info from the API and print it
def chuck():
    url = r'https://api.chucknorris.io/jokes/random'
    data = requests.get(url)
    tt = json.loads(data.text)

    print(tt['value'])
    return tt['value']

i = 0
while i < 10:
    text_get = chuck()
    #print(text_get)
    # Now, we create the text file and write the joke, which is stored into text_get, to the txt file
    f = open('chuck/results/results.txt', 'a+')
    f.write(text_get + "\n")
    f.close()
    i += 1
