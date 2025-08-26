# 2. Explain the purpose of the __init__() method in Python. Give an example using a Book class.

class Book:   # class 
    def __init__(self, title, author):
        self.title = title
        self.author = author

b = Book("The Psychology of Money", "Morgan Housel")
b1 = Book("Atomic Habits","James Clear")

print(f"First Book Details:{b.title},{b.author}")
print(f"Second Book Details:{b1.title},{b1.author}")