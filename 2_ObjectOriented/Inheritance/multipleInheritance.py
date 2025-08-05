class Dad:
    def walk(self):
        print("Dad walks slowly")

class Mom:
    def dance(self):
        print("Mom dance beautifully")

class Child(Dad, Mom):
    def model(self):
        print("Child is modeling")

ch=Child()
ch.model()
ch.dance()
ch.walk()
