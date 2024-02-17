import sqlite3

conn = sqlite3.connect("test1.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)")
conn.commit()
conn.close()