import tkinter as tk
import random

def change_background_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)

    color=f'#{r:02x}{g:02x}{b:02x}'

    root.config(bg=color)
    print(f"Background changed to {color}")
root=tk.Tk()
root.title("Python GUI")
root.geometry("300x400")

# adding label to window
label=tk.Label(root, text="Welcome coders")
label.pack()

def sayingHello():
    print("Button sensed")

# button clicked logic

# button= tk.Button(root, text="Click Me", command=sayingHello)
button= tk.Button(root, text="Click Me", command=change_background_color)
button.pack()

root.mainloop()