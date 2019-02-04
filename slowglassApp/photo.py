from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from slowglassApp.db import get_db

bp = Blueprint('photo', __name__, url_prefix='/photo')
# app = None

@bp.route('/')
def index():
	db = get_db()
	photos = db.execute(
		'SELECT id, title, subjects, webpage'
		' FROM photo'
		' ORDER BY id DESC'
	).fetchall()
	return render_template('photo/index.html', photos=photos)

@bp.route('/photo')
def photo():
	return render_template('photo/photo.html')

@bp.route('/create', methods=('GET', 'POST'))
def create():
	if request.method == 'POST':
		id = request.form['id']
		title = request.form['title']
		webpage = request.form['webpage']
		subjects = request.form['subjects']
		error = None

		if not title:
			error = 'Title is required.'

		if error is not None:
			flash(error)
		else:
			db = get_db()
			db.execute(
				' INSERT INTO photo (id,creator,publisher,title,p_date,medium,credit_line,'
				'accession_num,inscriptions,description,place_depicted,subjects,subjects_id,webpage)'
				' VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)',
				(id, None, None, title, None, None, None, None, None, None, None, subjects, None, webpage)
			)
			db.commit()
			return redirect(url_for('photo.index'))
	return render_template('photo/create.html')

@bp.route('/delete', methods=('POST','GET'))
def delete():
	if request.method == 'POST':
		id = request.form['id']
		error = None

		if not id:
			error = 'id is required.'

		if error is not None:
			flash(error)
		else:
		    db = get_db()
		    db.execute('DELETE FROM photo WHERE id = ?', (id,))
		    db.commit()
		    return redirect(url_for('photo.index'))
	return render_template('photo/delete.html')

	




