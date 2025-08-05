class GrandPa:
    def walk(self):
        print("GrandPa walks slowly")

class Dad(GrandPa):
    def dance(self):
        print("Dad dance beautifully")

class Child(Dad):
    def model(self):
        print("Child is modeling")

ch1=Child()
ch1.walk()
ch1.dance()
ch1.model()