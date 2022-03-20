
#Run a counter
import csv
import sqlite3

def get_db_connection():
  # connects to the executable sql
  conn = sqlite3.connect('database_back.db')
  conn.row_factory = sqlite3.Row
  return conn


conn = get_db_connection()
bias = 'democrat'
similar_articles = conn.execute("SELECT * FROM urls_back WHERE classification = ?", [bias] ).fetchall()

#print(similar_articles)
for art in similar_articles:
  print(art["url"])


conn.commit()
conn.close()