import tkinter as tk
root = tk.Tk()
root.title("Canvas Drawing")
root.geometry("300x250")
canvas = tk.Canvas(root, width=300, height=200, bg="white")
canvas.pack()

# Draw a line
canvas.create_line(10,10,200,10, fill="blue")

