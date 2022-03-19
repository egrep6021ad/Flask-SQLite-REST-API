
import bs4 as bs
import pandas as pd
import re #Regex import
import requests
import sys
#from seleniumrequests import Firefox
#@app.route('/scrapper/<url>')
#print(str(sys.argv))

url = sys.argv[1]
  
  # api-endpoint
  url_test = "https://www.cnn.com/2022/03/16/tech/instagram-parent-controls/index.html"
    
  # sending get request and saving the response as response object
  res = requests.get(url_test)
  content = res.content

  soup = bs.BeautifulSoup(content, 'html.parser') #lxml for faster speed

  #Get domain params from database

  #Make query according to the domain
  title  = soup.findAll("h1", class_="pg-headline")
  article = soup.find_all("div", class_="pg-side-of-rail pg-rail-tall__side") 

  print(title)
  #print(article)
  
  return '<h1>Scrap running! ' + url + ' </h1> <p> </p>'


#run_scrapping("mysecond.com")