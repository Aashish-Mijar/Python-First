# Write a program to elaborate different list methods. 

# create a list 

list = [ 0, 4, 7, "test", 6, "python"]
print("The first list is:", list)

# append method 

list.append("Deepa")
print("After adding some data in list:", list)

# insert method
list.insert(3, "true")
print("After inserting data in list:", list)

# remove method
list.remove("Deepa")
print("After removing data from list:", list)

# pop method
list.pop()
print("After popping data from list:", list)

# clear method
list.clear()
print("After clearing data from list:", list)

# extend method
list.extend(["Deepa", "true"])
print("After extending data in list:", list)