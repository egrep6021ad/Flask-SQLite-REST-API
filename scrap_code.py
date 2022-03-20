
import bs4 as bs
import pandas as pd
import re #Regex import
import requests
import sys
import sqlite3
import csv
import random
#from seleniumrequests import Firefox
#@app.route('/scrapper/<url>')
#print(str(sys.argv))
# Init. the cursor to interact with the database
#url = sys.argv[1]


def run_scrap(url):
  # api-endpoint
  #url_test = "https://www.cnn.com/2022/03/16/tech/instagram-parent-controls/index.html"
  conn = sqlite3.connect('database_back.db')
  conn.row_factory = sqlite3.Row
  # sending get request and saving the response as response object
  res = requests.get(url)
  content = res.content
  
  
  
  soup = bs.BeautifulSoup(content, 'html.parser') #lxml for faster speed
  
  #Get domain from the url
  #domain = re.findall('://www.*', url)
  domain = re.findall('://www.([\w\-\.]+)', url)

  #print(domain[0])
  
  ##Get the params from the url
  #default params
  title_tag = ""
  title = ""
  article = ""
  
  if( len(domain) > 0 ):
    print( "LENGTH =>" + str( len(domain)) )
    print(domain[0])
  
    #conn = get_db_connection()
    params = conn.execute("SELECT * FROM scrappingtags WHERE domain_tag = ?", [domain[0]]).fetchall()
    
    if( len(params) >0 ): #DOMAIN IS SUPPORTED 
      for param in params:
        #print(param["title_tag"] +" "+ param["article_tag"] )
        title_tag = param["title_tag"]
        article_tag = param["article_tag"]
    
    
      #Make query according to the domain tags
      title  = soup.findAll("h1", class_= title_tag )
      article = soup.find_all("div", class_= article_tag) 

    else: #DOMAIN IS NOT SUPPORTED 
      title = "Default title"
      article = content #Assign the whole page to the article
      
      
  #End if
  else:
    article = content

  
  result = {}
  result["title"] = title
  #result["article"] = article
  
      
  article = str(article)
  #print("ARTICLE BEGIN")
  #print( type(article) )
  #print(article)
  #Evaluating the article
  #counts = {}
  #counts["republican"] = 0
  #counts["democrat"] = 0
  count_dems = 0
  count_reps = 0
  with open('classification.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
      #print("Row=> " + row[0])
      if article.count(row[0]) > 0:
        #print("IN IF")
        #print("ROW ->" + row[0])
        #print(type(row[0]))
        #print(row[1])
        if str(row[1]) == 'republican': #space fixed in the csv file
          count_reps = count_reps + 1
          print("reps:" + str(count_reps))
        elif str(row[1]) == 'democrat':
          print("dems:" + str(count_dems))
          count_dems = count_dems + 1
  
  #result["bias"] = "nonbiased" #test
  if( count_reps > count_dems):
    result["bias"] = "republican"
    print("go for republican")
  elif( count_dems > count_reps):
    print("go for democrat")
    result["bias"] = "democrat"
  else:
    result["bias"] = "nonbiased"
    
  #result["bias"] = "democrat" #Demo
  
  #print("Bias => " + result["bias"])
  #Get 3 similars articles
  similar_articles = conn.execute("SELECT * FROM urls_back WHERE classification = ?", [ result["bias"] ]).fetchall()
  
  #print(similar_articles)
  results_tab = []
  results_tab.append( result["bias"] )

  #title = re.search(">(.*)<", str(title) )
  title = re.findall(">(.*)<", str(title)) #Regex expresion to get the title

  if( len(title)<1 ):
    results_tab.append("Default title")
  else:
    results_tab.append(title[0])
    
  res_suffled = []
  random.shuffle(similar_articles)
  res_suffled = similar_articles[:3]
  for art in res_suffled:
    results_tab.append(art["url"])
    #print(art["url"])
    
  #print(title)
  
  
  #print("RESULTS")
  #print(results_tab)
  
  conn.commit()
  conn.close()
  

  
  return results_tab
  