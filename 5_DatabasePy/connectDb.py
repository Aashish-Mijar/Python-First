import sqlite3
conn=sqlite3.connect("myFirstDb.db")
cursor=conn.cursor()
conn.close()