import sqlite3

connection = sqlite3.connect('searchHistory.db')

with open('searchHistorySchema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO urls (url, created,related_1,related_2,related_3,category) VALUES (?,?,?,?,?,?)",("example.com", "2022-03-18","test1.com","test2.com","test3.com","democrat"))

connection.commit()
connection.close()