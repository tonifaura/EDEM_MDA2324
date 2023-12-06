import pandas as pd

# auguacates=pd.read_excel("C:\\Users\\josan\\Desktop\\Aguacate producción.xlsx")


# aguacates_csv=pd.read_csv("C:\\Users\\josan\\Desktop\\aguacate.csv",delimiter=",")

# aguacates2_csv=pd.read_csv("C:\\Users\\josan\\Desktop\\aguacate2.csv",delimiter=";")

# print(aguacates2_csv)

import requests

randomUser="https://randomuser.me/api"

respuesta = requests.get(randomUser).json()
print(respuesta)