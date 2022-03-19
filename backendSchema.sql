DROP TABLE IF EXISTS urls_back;

CREATE TABLE urls_back (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT,
    created TEXT,
    classification VAR

);