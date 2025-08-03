# firstSet={1, 4, 5,6,9,2.4, 5}
# mySet=set()
# print(firstSet)
# print(mySet)
# print(type(mySet))


# ---Performing set operations
set1={"Apple", "kiwi", "orange"}
set2={"orange","banana", "avocado"}

# ---UNION
set3=set1 | set2
print("The union of set1 and set2 is ", set3)

# ----INTERSECTION
set4=set1 & set2
print("The intersection of set1 and set2 is ", set4)

# ---- set1 - set2
set5=set1 - set2
print("The different of set1 and set2 is ", set5)

# ---- set2 - set1
set6=set2 - set1
print("The different of set2 and set1 is ", set6)


set1.add("dragonFruit")
set1.remove("orange")
print(set1)