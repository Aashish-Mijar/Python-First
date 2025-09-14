import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
from tkinter import messagebox

# Initialize Sqlite database and create table if not existe
def init_db():
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS users(
                id  INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                gender TEXT,
                hobbies TEXT,
                country TEXT
                )
            """)
    
#  Save form data to database
def submit_form():
    name_val = name_entry.get().strip()
    gender_val = gender.get()
    country_val = country.get()
    hobbies_str = ", ".join(hobbies_val)

    if not name_val:
        messagebox.showerror("Error", "Name is required!")
        return
    
    try:
        with sqlite3.connect("from_data.db") as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users(name, gender, hobbies, country)VALUES (?,?,?,?)",
                (name_val, gender_val, hobbies_str, country_val)
            )
        messagebox.showinfo("Success", "Data saved successfully!")

        clear_form()
    except Exception as e:
        messagebox.showerror("Database Error", f"Could not save data:\n{e}")

# Clear all form inputs
def clear_form():
    name_entry.delete(0, tk,END)
    gender.set("Male")
    for var in hobby_vars.values():
        var.set(0)
    country.set("Nepali")

# Show saved records in a nice table with scrollbar
def view_records():
    try:
        with sqlite3.connect("form_data.db") as conn:
            cur = conn.cursor()
            cur.execute("SELECT id, name, gender, hobbies, country FROM uses ORDER BY id DESC")
            rows = cur.fetchall()
    execpt Exception as e:
       messagebox.showerro("Database Erro", f"Could not read data:\n{e}")
       return
    
    if not rows:
        messagebox.showinfo("Records", "No records found.")
        return
    
    win = tk.Toplevel(root)
    win.title("Saved Records")
    win.geometry("600x300")

    columns=("ID", "Name", "Gender", "Hobbies", "Country")
    tree = ttk.Treeview(win, columns=columns, show="headings")

 # Define headings
    for col in columns:
        tree.heading(col, text=col)

# Define column widths and alignment
tree.column("ID", width=40, anchor=tk.CENTER)
tree.column("Name", width=150)
tree.column("Gender", width=80, anchor=tk.CENTER)
tree.column("Hobbies", width=200)
tree.column("Country", width=80, anchor=tk.CENTER)

# Insert rows
for row in rows:
    tree.insert("", tk.END, values=row)

# Add vertical scrollbar
scrollbar = ttk.Scrollbar(win, orient=tk.VERTICAL, command=tree.yview)
tree.configure(yscroll = scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
tree.pack(expand=TRUE, fill=tk.BOTH)


 