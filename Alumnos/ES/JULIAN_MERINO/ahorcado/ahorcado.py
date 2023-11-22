#Let's read the csv and print it to check that it works
import csv
import random
#Let's create an abcdary list with all the letters:
abcdary = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
#print(abcdary[0])
#print(len(abcdary))
with open('palabras.csv') as file:
  next(file)
  data = file.read().splitlines()
  #print(data)
  # Iterate through the list of words to get length and play ahorcado:
  attempts = 0
  for word in data:
    word = word.lower()
    #print(word)
    #print(len(word))
    left = len(word)
    #print(left)
    i = 0
    while left != 0:
      while i < (len(abcdary) - 1):
        if word.count(abcdary[i]) == 0:
          attempts += 1
          #print(attempts)
          i += 1
        if word.count(abcdary[i]) != 0:
          #print(word.count(abcdary[i]))
          #print(abcdary[i])
          attempts += 1
          left -= word.count(abcdary[i])
          i += 1

file.close()
print(f'Total number of attempts in getting all {len(data)} words: {attempts}')