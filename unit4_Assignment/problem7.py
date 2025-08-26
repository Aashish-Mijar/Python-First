# 7. What is polymorphism in Python? Explain with an example where different classes have a method draw() and a function calls them.

class Pencil:
    def draw(self):
        print("Drawing with pencil is easy.")

class Brush:
    def draw(self):
        print("We can use brush for drawing.")

class Color:
    def draw(self):
        print("Color use for drawing and painting picture.")

def create_picture(tool):
    tool.draw()

p = Pencil()
b = Brush()
m = Color()

create_picture(p)
create_picture(b)
create_picture(m)

