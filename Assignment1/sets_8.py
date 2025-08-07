mySet1={2, 4, 5, 8}
mySet2={8, 9, 4, 3}

# print(mySet1)
# print(mySet2)

# ----- Union
print(mySet1.union(mySet2))

# ----- intersection
print(mySet1.intersection(mySet2))

# ----- difference
print(mySet1-mySet2)

# ---- Adding and removing element
mySet1.add(23)
print(mySet1)

mySet1.remove(2)
print(mySet1)