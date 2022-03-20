import sqlite3

connection = sqlite3.connect('searchHistory.db')

with open('searchHistorySchema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO urls (url, created) VALUES (?,?)",("example.com", "2022-03-18"))

connection.commit()
connection.close()