import os

from flask import Flask

# application factory function
def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'slowglassApp.sqlite'),
		# SQLALCHEMY_DATABASE_URI = 'mysql://root:password@server/db'
		# MYSQL_DATABASE_USER = 'root',
		# MYSQL_DATABASE_PASSWORD = 'root123!',
		# MYSQL_DATABASE_DB = 'slowglassApp',
		# MYSQL_DATABASE_HOST = 'localhost',
	)
	# app.config['MYSQL_DATABASE_USER'] = 'root'
	# app.config['MYSQL_DATABASE_PASSWORD'] = 'root123!'
	# app.config['MYSQL_DATABASE_DB'] = 'slowglassApp'
	# app.config['MYSQL_DATABASE_HOST'] = 'localhost'

	if test_config is None:
		# load the instance config, if it exists, when not testing
		app.config.from_pyfile('config.py', silent=True)
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)

	# ensure the instance folder exists
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	# a simple page that says hello
	@app.route('/hello')
	def hello():
		return 'Hello, World!'

	from . import db
	db.init_app(app)
	# from . import db_mysql
	# db_mysql.init_app(app)

	from . import home
	app.register_blueprint(home.bp)
	app.add_url_rule('/', endpoint='index')
	
	from . import photo
	# photo.app = app
	app.register_blueprint(photo.bp)



	return app