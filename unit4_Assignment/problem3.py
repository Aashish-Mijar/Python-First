# 3. What is the difference between defining class variables directly vs using the (instance variables) __init__() method? Show example output for both. 

# defining class variables directly (class variables)
print("Class Variables:")

class Company:
    company_name = "ABC Tech"

c = Company()

print("Company name:", c.company_name)

print()

#  __init__() method (instance variables) 

print("Instance Variables: ")

class Employee :
    def __init__(self, name, post):
        self.name = name
        self.post = post

employee = Employee("Dipisha", "Manager")

print("Name:", employee.name)
print("Post:", employee.post)
