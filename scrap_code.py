
import bs4 as bs
import pandas as pd
import re #Regex import
import requests
import sys
import sqlite3
import csv
#from seleniumrequests import Firefox
#@app.route('/scrapper/<url>')
#print(str(sys.argv))

# Init. the cursor to interact with the database
def get_db_connection():
    # connects to the executable sql
    conn = sqlite3.connect('database_back.db')
    conn.row_factory = sqlite3.Row
    return conn
  

url = sys.argv[1]
  
# api-endpoint
#url_test = "https://www.cnn.com/2022/03/16/tech/instagram-parent-controls/index.html"
  
# sending get request and saving the response as response object
res = requests.get(url)
content = res.content

print(content)

soup = bs.BeautifulSoup(content, 'html.parser') #lxml for faster speed

#Get domain from the url
domain = re.findall('://www.([\w\-\.]+)', url)
print(domain[0])

##Get the params from the url
#default params
title_tag = ""
article = ""

conn = get_db_connection()
params = conn.execute("SELECT * FROM scrappingtags WHERE domain_tag = ?", (domain) ).fetchall()
for param in params:
  print(param["title_tag"] +" "+ param["article_tag"] )
  title_tag = param["title_tag"]
  article_tag = param["article_tag"]

  
#Make query according to the domain tags
title  = soup.findAll("h1", class_= title_tag )
article = soup.find_all("div", class_= article_tag) 

#test
#article = "lorem ipsum sheep dolar si abet cramer loyalism protestantism"

result = {}
result["title"] = title
result["article"] = article

#Evaluating the article
counts = {}
counts["republican"] = 0
counts["democrat"] = 0

with open('classification.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter=',')
  line_count = 0
  for row in csv_reader:
    if( row[1] == 'republican' ):
      counts["republican"] += float(article.count(row[0]))
    else:
      counts["democrat"] += float(article.count(row[0]))

if( counts["republican"] > counts["democrat"] ):
  result["bias"] = "republican"
elif( counts["democrat"] > counts["republican"] ):
  result["bias"] = "democrat"
else:
  result["bias"] = "none"

#Get 3 similars articles
similar_articles = conn.execute("SELECT * FROM urls_back WHERE classification = ?", [ result["bias"] ]).fetchall()

#print(similar_articles)
articles_tab = []
for art in similar_articles:
  articles_tab.add(art["url"])
  print(art["url"])
  
print(title)
print(articles_tab)

conn.commit()
conn.close()

#Classification - 3 Articles


#print(result)

#return result


#run_scrapping("mysecond.com")