import tkinter as tk

root=tk.Tk()
root.title("Check Button Window")
root.geometry("300x300")

label=tk.Label(root, text="Check Button")
label.pack()

var1=tk.IntVar()
var2=tk.IntVar()

tk.Checkbutton(root, text="Python", variable=var1).pack()
tk.Checkbutton(root, text="Java", variable=var2).pack()

root.mainloop()