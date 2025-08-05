class Dad:
    def walk(self):
        print("Dad walks")

class child1(Dad):
    def dance(self):
        print("Child 1 dances well")

class child2(Dad):
    def sing(self):
        print("Child 2 sings well")

child1=child1()
child1.dance()
child1.walk()

child2=child2()
child2.sing()
child2.walk()
