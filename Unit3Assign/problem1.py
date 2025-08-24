# 1. Write a Python program to demonstrate the use of the following list methods: append(), insert(), sort(), remove(), reverse(), min(), max().

list = [1, 0, 2, 5, 4, 3, 29 ]
print("This is original list:",list)

# use the different methods in list 

  #append()
list.append(7)

print("The list after using append method:",list)

    # insert()
list.insert(2, 9)  # index, value
print("The list after use insert method:", list)

     # sort()
list.sort()
print("This is sorted list:", list)

     # remove()
list.remove(0)
print("This is new list after use remove method:",list)
     
     # reverse()
list.reverse()
print("This is reverse list:",list)

    # min()
minimum = min(list)
print("The minimum value of this list is:", minimum)

    # max 
maximum = max(list)
print("This is the maximum value of this list:",maximum)

