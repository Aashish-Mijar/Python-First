import sqlite3
def create_students(name, age):
    try:
        conn=sqlite3.connect("myFirstDb.db")
        cursor=conn.cursor()
        cursor.execute("INSERT INTO students(name, age) VALUES(?,?)",(name, age))
        print("Students added successfully")
    except sqlite3.Error as e:
      print(f"Error:{e}")

    finally:
       if conn:
          conn.close()

create_students("Alice", 19)