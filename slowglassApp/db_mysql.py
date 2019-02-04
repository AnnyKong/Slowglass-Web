from flaskext.mysql import MySQL


import click
from flask import current_app, g
from flask.cli import with_appcontext

def init_app(app):
	# tells Flask to call that function when cleaning up after returning the response
	app.teardown_appcontext(close_db)
	# adds a new command that can be called with the flask command
	app.cli.add_command(init_db_command)
	 
	# MySQL configurations

	

def init_db(app):
	db = get_db()
	app.config['MYSQL_DATABASE_USER'] = 'root'
	app.config['MYSQL_DATABASE_PASSWORD'] = 'root123!'
	app.config['MYSQL_DATABASE_DB'] = 'slowglassApp'
	app.config['MYSQL_DATABASE_HOST'] = 'localhost'

	conn = db.connect()
	cursor = conn.cursor()

	with current_app.open_resource('schema.sql') as f:
		db.executescript(f.read().decode('utf8'))
	db.init_app(current_app)

# defines a command line command called init-db
# that calls the init_db function and shows a success message to the user
@click.command('init-db')
@with_appcontext
def init_db_command():
	"""Clear the existing data and create new tables."""
	init_db()
	click.echo('Initialized the database.')

# returns a database connection
def get_db():
	# if 'db' not in g:
	# 	g.db = sqlite3.connect(
	# 		current_app.config['DATABASE'],
	# 		detect_types=sqlite3.PARSE_DECLTYPES
	# 	)
	# 	g.db.row_factory = sqlite3.Row 
	if 'db' not in g:
		g.db = MySQL()


	return g.db

def close_db(e=None):
	db = g.pop('db', None)

	if db is not None:
		db.close()