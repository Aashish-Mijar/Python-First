class Base1:
    def greet(self):
        print("Saying Hello")

class Base2:
    def greet(self):
        print("Saying Namaste")

class Base3:
    def greet(self):
        print("Saying Bonjour")

def called(person):
    person.greet()

called(Base1())
called(Base2())
called(Base3())