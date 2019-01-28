DROP TABLE IF EXISTS photo;
DROP TABLE IF EXISTS subject;

CREATE TABLE photo (
	id INTEGER PRIMARY KEY,
	creator TEXT,
	publisher TEXT,
	title TEXT NOT NULL, -- NOT SURE
	p_date TEXT,
	medium TEXT,
	credit_line TEXT,
	accession_num TEXT,
	inscriptions TEXT,
	description TEXT, 
	place_depicted TEXT,
	subjects TEXT,
	subjects_id INTEGER REFERENCES subject(subjects_id),
	webpage TEXT NOT NULL
);

CREATE TABLE subject (
	subjects_id INTEGER PRIMARY KEY,
	s0 TEXT,
	s1 TEXT,
	S2 TEXT,
	s3 TEXT,
	s4 TEXT,
	S5 TEXT,
	s6 TEXT,
	s7 TEXT,
	S8 TEXT,
	s9 TEXT
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