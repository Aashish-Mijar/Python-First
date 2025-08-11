import tkinter as tk

root=tk.Tk()
root.title("My first App")
root.geometry("300x200")

label=tk.Label(root, text="Hello, World")
label.pack()

def say_hello():
    print("Button Clicked")
button=tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()

