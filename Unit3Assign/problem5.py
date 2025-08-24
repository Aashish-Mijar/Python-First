# 5. Write down three differences between lists and tuples. Also, write a Python program to create a tuple and show that it is immutable.  

 # list 
list = ["a", "b", "c", "d", "e"]  # list is mutable because we can perform different operation.
print("The original list:", list)
list.append("f")
print("This is new list: ", list)

# tuple
t = (1, 2, 3, 4, 5, 6)
print("The original tuple:",t)
t.append(7)  # we can't perform append() operation in tuple.
      # tuple is immutable, when we try to perform different operation then it shows the "('tuple' object has no attribute 'append')" this error message. 
