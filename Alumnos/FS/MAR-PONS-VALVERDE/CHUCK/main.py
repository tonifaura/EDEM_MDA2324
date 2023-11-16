print('Hola Mundo')

import requests
from requests.models import Response
URL: str= 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)
data = json.loads(response.text)
print(data['value'])
