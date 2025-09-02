# set operation in python:
a = {1, 2, 3, 4, 5}
b = {4,5, 6,7, 8,9}

# uninon set
c = a|b
print(f"The union of a and b set is:{c}" )

# intersection set
d = a&b
print(f"The intersection of a and b set is: {d}")

# a-b
e = a-b
print(f" The different between a and b is : {e}")

# b- a 
f = b-a 
print(f" The different between b and a is: {f} ")

# add item
a.add(11)
print(a)

# remove item
b.remove(9)
print(b)

