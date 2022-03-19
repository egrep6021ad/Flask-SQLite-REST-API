from flask import Flask, request, render_template
from flask_cors import CORS
import sqlite3
from threading import Thread
import sys
import datetime
import os

#from scrap_code import run_scrapping

# Naming convention to wrap the whole app as a flask app
app = Flask('app')
# Cors needs to be enabled for the cross origin issues that happend with api calls
CORS(app)


# Init. the cursor to interact with the database
def get_db_connection():
    # connects to the executable sql
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
  
# This is the main web view for backend (not visible to users, admins only)
@app.route('/')
def index():
  # GET request is main to index url  -> query db
  conn = get_db_connection()
  # Select all urls saved in the db
  articles = conn.execute("SELECT * FROM urls").fetchall()
  # Close curos
  conn.close()
  # render the data in the easy view html 
  return render_template('backendView.html',urls=articles)

@app.route('/test_scrap')
def test_index():
  print("test 2")
  #return run_scrapping("myurl.com")

  
# End point for POST requests from the front end (front end sending article -> backend)
@app.route('/postArticle', methods=['POST'],strict_slashes=False)
def postArticle():
    if request.method == 'POST':
      data = request.get_json(force=True) #Force stops flask from saying json is none- type
      article = data['value']
      # Console log the data to make sure it came
      print("Data from front-end POST:")
      print(article,file=sys.stderr)
      created = str(datetime.date.today())

      os.system("python scrap_code.py {}".format(article))
      # Open Db cursor
      conn = get_db_connection()
      # Inset data into db
      conn.execute("INSERT INTO urls (url,created) VALUES(?,?)",(article,created ))
      # Push data
      conn.commit()
      # Close cursor
      conn.close()
      # Log sucess Message
      print("exiting without errors!")
      # Render the easy view html
      return render_template('backendView.html')
  
# GET Endpoint for front -end getting specific articles back
@app.route('/getArticles', methods=['GET'],strict_slashes=False)
def getArticles():

  date = "2022-03-18"
  #date = str(datetime.date.today())
  
  conn = get_db_connection()
  articles = conn.execute("SELECT * FROM urls WHERE created = ? ",(date)).fetchall()
  print(articles,file=sys.stderr)
  conn.close()
  return ("done")

      
# Run backend application in its own on its port
def run():
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(host='0.0.0.0', port=7000)
t = Thread(target=run)
t.start()


