# 7. Write a Python program to read and display the contents of note.txt. 

file = open("unit 5_Assignment/note.txt", "r")
message = file.read()
print(message)
file.close()
