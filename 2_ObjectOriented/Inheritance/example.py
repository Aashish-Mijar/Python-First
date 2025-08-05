# Program applying where vehicle class.

class Vehicle:
    def drive(self):
        print("Drive your car")
    
    def honk(self):
        print("Car can honk differently")

class Car(Vehicle):
    def color(self):
        print("Car's color is customizable")

obj1=Vehicle()
obj1.drive()
obj1.honk()

