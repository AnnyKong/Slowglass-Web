DROP TABLE IF EXISTS photo;

CREATE TABLE photo (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	creator TEXT,
	publisher TEXT,
	title TEXT NOT NULL, -- NOT SURE
	p_date TEXT,
	medium TEXT,
	credit_line TEXT,
	accession_num TEXT,
	inscriptions TEXT,
	description TEXT, 
	place depicted TEXT,
	subjects TEXT,
	webpage TEXT NOT NULL
);

-- DROP TABLE IF EXISTS user;
-- DROP TABLE IF EXISTS post;

-- CREATE TABLE user (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   username TEXT UNIQUE NOT NULL,
--   password TEXT NOT NULL
-- );

-- CREATE TABLE post (
--   id INTEGER PRIMARY KEY AUTOINCREMENT,
--   author_id INTEGER NOT NULL,
--   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
--   title TEXT NOT NULL,
--   body TEXT NOT NULL,
--   FOREIGN KEY (author_id) REFERENCES user (id)
-- );