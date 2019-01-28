# A Blueprint is a way to organize a group of related views and other code. 
# Rather than registering views and other code directly with an application, 
# they are registered with a blueprint. 
# Then the blueprint is registered with the application when it is available in the factory function.
import functools

from flask import (
	Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from slowglassApp.db import get_db

# bp = Blueprint('auth', __name__, url_prefix='/auth')
bp = Blueprint('home', __name__)

# When Flask receives a request to /home, 
# it will call the home view and use the return value as the response.
@bp.route('/home', methods=('GET', 'POST'))
def home():
	# If the user submitted the form, request.method will be 'POST'. 
	# In this case, start validating the input.
	if request.method =='POST':
		# username = request.form['username']
  #       password = request.form['password']
		db = get_db()
		error = None

		# template for using db

		# The database library will take care of escaping the values 
		# so you are not vulnerable to a SQL injection attack.

		# if not <>:
		# 	error = '<> is required.'
		# elif not <>:
		# 	error = '<> is required.'
		# elif db.execute(
		# 	'SELECT webpage FROM photo WHERE id = ?', (id)
		# ).fetchone() is  None:
		#	# returns one row from the query
		# 	error = 'Photo {} not found.'.format(id)

		# if error is None:
		# 	db.execute(
		# 		'INSERT INTO photo (id, ..., webpage) VALUES (?, ..., ?)',
		# 		(id, ..., webpag)
		# )
		# 	db.commit()
		#   # url_for() generates the URL for the login view based on its name.
		# 	return redirect(url_for('auth.login'))
		# 
		#  # If validation fails, the error is shown to the user. 
		#  # flash() stores messages that can be retrieved when rendering the template.
		#  flash(error)

		# session template
		# if error is None:
  #           session.clear()
  #           session['user_id'] = user['id']
  #           return redirect(url_for('index'))

	return render_template('home.html')








# Now that the user’s id is stored in the session, 
# it will be available on subsequent requests. 
# At the beginning of each request, if a user is logged in 
# their information should be loaded and made available to other views.
# 
# bp.before_app_request() registers a function that runs before the view function, 
# no matter what URL is requested. load_logged_in_user checks if a user id is stored 
# in the session and gets that user’s data from the database, storing it on g.user, 
# which lasts for the length of the request. If there is no user id, or if the id doesn’t 
# exist, g.user will be None.
# 
# @bp.before_app_request
# def load_logged_in_user():
#     user_id = session.get('user_id')

#     if user_id is None:
#         g.user = None
#     else:
#         g.user = get_db().execute(
#             'SELECT * FROM user WHERE id = ?', (user_id,)
#         ).fetchone()


# def login_required(view):
#     @functools.wraps(view)
#     def wrapped_view(**kwargs):
#         if g.user is None:
#             return redirect(url_for('auth.login'))

#         return view(**kwargs)

#     return wrapped_view