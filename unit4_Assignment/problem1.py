# 1. Write a Python class called Laptop that has two attributes: brand and color. Create two objects with different values and print their details. 

class Laptop: 
    brand = ""      # class attribute
    color = ""

laptop1 = Laptop()  # object 1 
laptop2 = Laptop()  # object 2

laptop1.brand = "Dell"
laptop1.color = "Black"

laptop2.brand = "HP"
laptop2.color = "Silver"

print(f"This is the first laptop details: {laptop1.brand}, {laptop1.color}")
print(f"This is the second laptop details: {laptop2.brand}, {laptop2.color}")