# 4. Define a class Animal with a method speak(). Then define a child class Dog that inherits from Animal and adds a method bark(). Create a Dog object and call both methods. 

class Animal:          # class
    def speak(self):   # method 
        print("Animal makes a sound.")

class Dog(Animal):     # inherit class
    def bark(self):    # method
        print("Dog barks")

dog = Dog()     # object create
dog.speak()
dog.bark()