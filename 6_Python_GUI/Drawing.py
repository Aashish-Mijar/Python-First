import tkinter as tk
root = tk.Tk()
root.title("Canvas Drawing")
root.geometry("300x250")
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw a line
canvas.create_line(10,10,200,10, fill="blue")

# Draw a rectangle
canvas.create_rectangle(50, 50, 150, 100, fill="green")

# Draw an oval (Circle/ellipse)
canvas.create_oval(70, 120, 170, 170, fill="red")

# Draw text
canvas.create_text(150, 190, text="Canvas is fun!", fill="black")

root.mainloop()