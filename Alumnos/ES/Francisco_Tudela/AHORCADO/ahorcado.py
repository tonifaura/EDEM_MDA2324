import csv
import pandas as pd
import csv
import time
palabras_dfr = pd.read_csv("Palabras.csv")

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

words_list = palabras_dfr["Palabras"].tolist()

for word in words_list:
    leng= len(word)
    print(leng)
    while leng > 0:
        i = 0
        guess = abecedario
        if guess in word:
            leng -= 1
        