import sqlite3

connection = sqlite3.connect('database_back.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO urls_back (url, created, classifiation) VALUES (?,?,?)",("example.com", "2022-03-18", "Left Test"))

connection.commit()
connection.close()