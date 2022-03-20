import sqlite3

connection = sqlite3.connect('database_back.db')

with open('backendSchema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.foxnews.com/politics/fauci-warns-americans-could-face-more-lockdowns-amid-spread-of-new-covid-19-variant", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.nytimes.com/2022/03/19/opinion/parents-schools.html", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.theguardian.com/us-news/2022/mar/19/stacey-abrams-president-earth-star-trek-georgia-governor", "democrat"))


#Init for tags
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("cnn.com", "pg-headline", "pg-side-of-rail pg-rail-tall__side"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("foxnews.com", "headline", "article-body"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("theguardian.com", "dcr-125vfar", "article-body"))



connection.commit()
connection.close()