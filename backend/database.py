# backend/database.py
import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS messages
                  (id INTEGER PRIMARY KEY, message TEXT)''')

conn.commit()
conn.close()
