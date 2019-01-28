import os

from flask import Flask

# application factory function
def create_app(test_config=None):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path, 'slowglassApp.sqlite'),
	)

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

	from . import home
	app.register_blueprint(home.bp)

	# from flask import (
	# Blueprint, flash, g, redirect, render_template, request, session, url_for
	# )

	# # When Flask receives a request to /home, 
	# # it will call the home view and use the return value as the response.
	# @app.route('/home', methods=('GET', 'POST'))
	# def home():
	# 	# If the user submitted the form, request.method will be 'POST'. 
	# 	# In this case, start validating the input.

	# 	return render_template('home/home.html')

	return app