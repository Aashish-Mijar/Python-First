# 8. Suppose you have a file names.txt with several names (one per line). Write a program that reads and prints each name using a loop.

file = open("unit 5_Assignment/names.txt", "r")

for line in file:
    print(line.strip())

file.close()