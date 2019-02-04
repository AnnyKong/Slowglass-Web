from flask_sqlalchemy import SQLAlchemy


import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
	# tells Flask to call that function when cleaning up after returning the response
	app.teardown_appcontext(close_db)
	# adds a new command that can be called with the flask command
	app.cli.add_command(init_db_command)

# defines a command line command called init-db
# that calls the init_db function and shows a success message to the user
@click.command('init-db')
@with_appcontext
def init_db_command():
	"""Clear the existing data and create new tables."""
	init_db()
	click.echo('Initialized the database.')

def init_db():
	db = get_db()

	# with current_app.open_resource('schema.sql') as f:
	# 	db.executescript(f.read().decode('utf8'))
	db.create_all()

# returns a database connection
def get_db():
	if 'db' not in g:
		g.db = SQLAlchemy(app)

	return g.db

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()