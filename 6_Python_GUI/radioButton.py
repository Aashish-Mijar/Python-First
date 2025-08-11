import tkinter as tk

root=tk.Tk()
root.title("Radio Button")
root.geometry("300x300")

label=tk.Label(root, text="Radio Button")
label.pack()

choice=tk.StringVar()
tk.Radiobutton(root, text="Male", variable=choice, value="Male").pack()
tk.Radiobutton(root, text="Female",variable=choice, value="Female").pack()

root.mainloop()