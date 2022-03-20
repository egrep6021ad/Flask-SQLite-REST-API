import sqlite3

connection = sqlite3.connect('database_back.db')

with open('backendSchema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

#democrat leaning sites
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.foxnews.com/politics/fauci-warns-americans-could-face-more-lockdowns-amid-spread-of-new-covid-19-variant", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.nytimes.com/2022/03/19/opinion/parents-schools.html", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.theguardian.com/us-news/2022/mar/19/stacey-abrams-president-earth-star-trek-georgia-governor", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://nypost.com/2022/03/19/thousands-of-ukrainians-forcibly-taken-to-russian-camps-reports/", "democrat"))
#republican leaning sites
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/magazine/2022/02/23/democrats-losing-culture-war-messaging-shift-00011091", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.foxbusiness.com/economy/chinese-official-calls-sanctions-russia-increasingly-outrageous", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/2022/03/01/state-of-the-union-reset-biden-democrats-00012567", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/magazine/2022/03/04/pennsylvania-rural-democrats-trump-neighbors-00008915", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.theguardian.com/us-news/2022/mar/13/barr-trump-should-not-be-president-but-lesser-of-two-evils-compared-to-us-left", "republican"))

#DOMIANS SUPPORTED - init for tags
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("cnn.com", "pg-headline", "pg-rail-tall__wrapper"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("nypost.com", "pg-headline", "pg-rail-tall__side"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("thegaurdian.com", "pg-headline", "pg-rail-tall__side"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("foxnews.com", "headline", "article-body"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("theguardian.com", "dcr-125vfar", "dcr-185kcx9"))



connection.commit()
connection.close()