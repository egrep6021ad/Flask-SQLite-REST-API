from flask import Flask
# Scraping should be own file
from selenium import webdriver
import bs4 as bs
import pandas as pd
import re #Regex import
import requests
#from seleniumrequests import Firefox
@app.route('/scrapper/<url>')
def run_scrapping(url):
  # Simple usage with built-in WebDrivers:
  # importing the requests library

  
  # api-endpoint
  url = "https://www.cnn.com/2022/03/16/tech/instagram-parent-controls/index.html"
    
  # location given here
  #location = "delhi technological university"
    
  # defining a params dict for the parameters to be sent to the API
  #PARAMS = {'address':location}
    
  # sending get request and saving the response as response object
  res = requests.get(url)
  content = res.content

  soup = bs.BeautifulSoup(content, 'html.parser') #lxml for faster speed
  title  = soup.findAll("h1", class_="pg-headline")
  article = soup.find_all("div", class_="pg-side-of-rail pg-rail-tall__side") 

  print(title)
  print(article)
  
  return '<h1>Scrap running! ' + url + ' </h1> <p> </p>'