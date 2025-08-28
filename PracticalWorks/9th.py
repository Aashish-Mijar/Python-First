# Write program to perform set operations. 

# create a set 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# union 
U = set1 | set2
print("Union of this set:", U)

# intersection 
I =  set1 & set2 
print("Intersection of this set:", I)

# difference 
D1 = set1 - set2
print("The first difference of this set:", D1)

D2 = set2 - set1
print("The second difference of this set:", D2)

# symmetric difference
S = set1 ^ set2
print("Symmetric difference of this set:", S)