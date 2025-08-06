file = open("example.txt", "r")

# ----method one
# content = file.readlines()
# print(content)

# ----method 2
for line in file:
    print(line)
    
file.close()