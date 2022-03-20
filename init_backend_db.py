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
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.theguardian.com/us-news/2021/nov/06/joe-biden-infrastructure-bill-democrats-monumental-step-forward", "democrat"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.usnews.com/news/education-news/articles/2022-02-02/congressional-democrats-take-aim-at-efforts-to-ban-critical-race-theory", "democrat"))

#republican leaning sites
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/magazine/2022/02/23/democrats-losing-culture-war-messaging-shift-00011091", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.foxbusiness.com/economy/chinese-official-calls-sanctions-russia-increasingly-outrageous", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/2022/03/01/state-of-the-union-reset-biden-democrats-00012567", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politico.com/news/magazine/2022/03/04/pennsylvania-rural-democrats-trump-neighbors-00008915", "republican"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.theguardian.com/us-news/2022/mar/13/barr-trump-should-not-be-president-but-lesser-of-two-evils-compared-to-us-left", "republican"))

#nonbiased leaning sites
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.aljazeera.com/opinions/2022/3/13/a-hitchhikers-guide-to", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.politicopro.com/blog/is-politico-right-or-left-leaning/", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.thefactual.com/blog/is-politico-biased/", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.reuters.com/business/futures-dip-three-day-rally-cools-2022-03-18/", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.washingtonexaminer.com/opinion/the-cdc-gets-a-failing-grade-for-the-pandemic", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://www.businessinsider.com/europe-covid-surge-precedes-us-spike-experts-say-2022-3", "nonbiased"))
cur.execute("INSERT INTO urls_back (url, classification) VALUES (?,?)",("https://apnews.com/article/covid-science-health-business-smoking-a08f61558a0e742e2ad22daee68d03c9", "nonbiased"))

#DOMIANS SUPPORTED - init for tags
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("cnn.com", "pg-headline", "pg-rail-tall__wrapper"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("nypost.com", "headline--single", "entry-content")) #single__content entry-content m-bottom 
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("foxnews.com", "headline", "article-body"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("politico.com", "headline", "story-text"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("foxbusiness.com", "headline", "article-body"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("reuters.com", "text__text__1FZLe text__dark-grey__3Ml43 text__medium__1kbOh text__heading_2__1K_hh heading__base__2T28j heading__heading_2__3Fcw5", "article-body__content__3VtU3 paywall-article"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("washingtonexaminer.com", "ArticlePage-headline", "RichTextArticleBody-body"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("businessinsider.com", "post-headline ", "content-lock-content"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("apnews.com", "Component-heading-0-2-44", "Article"))
cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("theguardian.com", "dcr-125vfar", "article-body-commercial-selector article-body-viewer-selector  dcr-ucgxn1"))
#cur.execute("INSERT INTO scrappingtags (domain_tag, title_tag, article_tag) VALUES (?,?,?)",("usnews.com", "Heading-sc-1w5xk2o-0", "ArticleBody__ArticleBox-u2fa96-2")) #Heading-sc-1w5xk2o-0


connection.commit()
connection.close()