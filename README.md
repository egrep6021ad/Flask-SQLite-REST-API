
NOTES ON WHAT TO DO 

We input a the website url of the article. The program scans the the text for bias indicating words such as rightwing, left wing, liberal. 

STEPS BACKEND
1- Create a massive database of key words and phrases for each political category.
  Q: How to determine which word is from which political category?
2- Scap the article
  Q: How do we make sure we have the right text content ?
3- Run a function to identify all the words in the article and categorise the article according to the words it contains
  
4- Return the classification and three related articles urls. 

FLOW: front end -> url ->flask api -> classification with python -> json of urls similar as return to -> frontend




-------------
We can maintain a database of supported local media websites
Provide an evaluation acording to the following criteria
- Political alignment, Violence, Racial issue, Minorities community

Can we use Google cloud in our work ?
Can we add twilio inside the app ? 


-----
python scraper and imports need to be in their own file, outside of main.py which hosts flask app for backend