# 2. Create a list of squares of all even numbers between 1 and 20 using list comprehension.

squares = []  
for a in range(1, 21):    # for loop 
    if a% 2==0: # condition for even numbers
         squares.append(a*a) 
print(squares)   # print value 
