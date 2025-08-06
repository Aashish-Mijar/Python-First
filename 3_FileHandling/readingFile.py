# reading file by opening in read mode
file = open("notes.txt", "r")
data=file.read()
print(data)
file.close()