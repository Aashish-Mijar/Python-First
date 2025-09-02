# string slicing in python:

word = "Programming"

# print all word "Programming"
print(word)

# print "Progra"
print(word[0:6])

# print ""Progra" starting with start word.
print(word[:6])

# print "gramming" start with index 3 and continue to the end. 
print(word[3:])

# print "Porming" skip step by 2. 
print(word[::2])
# print(word[0::2])

# print "rgamn"
print(word[1::2])

# print "Programming" into reversed
print(word[::-1])

# print "rga"
print(word[5:2:-1])

# print "imm"
print(word[8:5:-1])

#print "min"
print(word[7:10])

# print "min" reverse
print(word[-4:-1])