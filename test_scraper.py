from scrap_code import *
import sqlite3
import random
url = sys.argv[1]

conn = sqlite3.connect('database_back.db')
conn.row_factory = sqlite3.Row

results_tab = []

#Get the IDs
similar_articles = conn.execute("SELECT * FROM urls_back WHERE classification = 'republican' ").fetchall()

#print(similar_articles)
#for article in similar_articles:
    #print( article["url"] )
  
random.shuffle(similar_articles)
res = similar_articles[:3]


final_tab = []
for art in res:
    final_tab.append(art["url"])

#print("FINAL")
#print(final_tab)

value = run_scrap(url)

print(value)
#(.*)