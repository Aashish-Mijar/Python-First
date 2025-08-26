# 6. Write a Python program using multiple inheritance where:
"""   •Chef class can cook
      •Driver class can drive
      •Employee class inherits both and can also attend meetings   """

class Chef:
    def cook(self):
        print("Chef can cook somthing new.")

class Driver:
    def drive(self):
        print("The driver can drive properly.")

class Employee(Chef, Driver):
    def meeting(self):
        print("Employee can inheits both data from to different class.")


e = Employee()
e.cook()
e.drive()
e.meeting()