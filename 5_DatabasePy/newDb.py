import sqlite3
conn=sqlite3.connect("thirdDb.db")
cursor=conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS students(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT,
               age INTEGER)
               """ )

cursor.execute("INSERT INTO students(name, age)VALUES(?,?)",("Aashish", 20))
cursor.execute("SELECT * FROM students")
rows=cursor.fetchall()
for row in rows:
    print(row)

conn.close()