# Slowglass Web Application

## Project layout
```
/home/user/Projects/flask-tutorial
├── slowglassApp/          a Python package containing application code and files.
│   ├── __init__.py
│   ├── db.py
│   ├── schema.sql
│   ├── home.py
│   ├── photo.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── photo/
│   │   │   ├── index.html
│   │   │   └── photo.html
│   │   └── /
│   │       ├── .html
│   │       ├── .html
│   │       └── .html
│   └── static/
│       └── style.css
├── tests/         			a directory containing test modules.
│   ├── conftest.py
│   ├── data.sql
│   ├── test_db.py
│   ├── .py
│   └── .py
├── setup.py
└── MANIFEST.in
```

## Instructions
1. Execute `sh run_me_first.sh` or
	```
	export FLASK_APP=slowglassApp
	export FLASK_ENV=development
	```
2. Run the App
	```
	flask run
	```
	You’ll see output similar to this:
	```
	* Serving Flask app "flaskr"
	* Environment: development
	* Debug mode: on
	* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	* Restarting with stat
	* Debugger is active!
	* Debugger PIN: 855-212-761
	```
	Visit <http://127.0.0.1:5000/> in a browser. You’re now running your Flask web application!
3. Run the init-db command:
	```
	flask init-db
	```
	You'll see output:
	```
	Initialized the database.
	```
	There will now be a `flaskr.sqlite` file in the `instance` folder in your project.

