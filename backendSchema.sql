DROP TABLE IF EXISTS urls_back;
DROP TABLE IF EXISTS scrappingtags;

CREATE TABLE urls_back (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    classification TEXT

);

CREATE TABLE scrappingtags(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    domain_tag TEXT,
    title_tag TEXT,
    article_tag TEXT
);

--CREATE TABLE keywords(
 --   id INTEGER PRIMARY KEY AUTOINCREMENT,
  --  label VARCHAR(200)  
--);