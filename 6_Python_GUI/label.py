import tkinter as tk
root = tk.Tk()
root.title("Frame Example")
root.geometry("400x400")

top_frame=tk.Frame(root)
top_frame.pack()

# ------ Name Label
label1=tk.Label(top_frame, text="Name")
label1.pack(side="left")

entry1=tk.Entry(top_frame)
entry1.pack(side="left")

# -------- Gender Label
# label2=tk.Label(top_frame, text="Radio Frame")
# label2.pack()

choice=tk.StringVar()
tk.Radiobutton(root, text="Male", variable=choice, value="Male").pack()
tk.Radiobutton(root, text="Female", variable=choice, value="Female").pack()

# -------- Hobby label

var1=tk.IntVar()
var2=tk.IntVar()
var3=tk.IntVar()

tk.Checkbutton(root, text="Python", variable=var1).pack()
tk.Checkbutton(root, text="Java", variable=var2).pack()
tk.Checkbutton(root, text="C Sharp", variable=var3).pack()
root.mainloop()

