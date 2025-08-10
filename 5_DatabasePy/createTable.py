import os
import sqlite3
db_file="myFirstDb.db"

if os.path.exists(db_file):
    os.remove(db_file)
try:
    conn=sqlite3.connect(db_file)
    cursor=conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER
 )
""")
    conn.commit()
    print("Database and table created successfully.")
    
except sqlite3.Error as e:
    print(f"An error occurred: {e}")

finally:
    if conn:
        conn.close()


        