# List in python 
# Used to store multiple items in a single variable. built in data types
# ordered and changeable. Allows duplicate members


myList=['apple', 'banana','cherry', 'cherry']
# print(myList)
# print(len(myList))   

# list with different datatypes
allList=['Aashish', 2, 'Education', 20]
# print(allList)
# print(allList[-4])

# to find the type of --
# print(type(allList))

# list() Constructor
thisList=list(("apple", "ball", "cat", "dog", "egg", "fish"))
# print(thisList[2:4])
# print(thisList[:4])
# print(thisList[-4:-1])

if "apple" in thisList:
    print("Yes, 'apple' is the list")