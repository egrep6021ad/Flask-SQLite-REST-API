DROP TABLE IF EXISTS urls;

CREATE TABLE urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    created TEXT,
    related_1 TEXT,
    related_2 TEXT,
    related_3 TEXT,
    category TEXT

);