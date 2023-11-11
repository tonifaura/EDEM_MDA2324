f = open("prueba.txt", "a")
f.write("\nSee you soon\nHola que tal!")
f.close()

#open and read the file after the appending:
f = open("prueba.txt", "r")
print(f.read())