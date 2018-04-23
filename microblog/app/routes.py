import sys
import psycopg2
sys.path.insert(0,'C:\\Users\\htaleshi\\Desktop\\microblog\\app\\py_scripts')
import do_something as d
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home',user=user)


@app.route('/py_scripts/do_something.py')
def my_link():
	d.print_to_server()
	return "hello"

