import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template#, flash
from contextlib import closing

#DATABASE = '/tmp/flaskr.db'
DATABASE = 'BDZ.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return 'Welcome to the Brilliant Dashing Zestful system for buying tickets :)'

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select seat_number, name,  id_number, destination, price from entries order by seat.number asc')
    #entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]--> това няма да е така
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST']) # ще се прави от служител на БДЖ
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (name, id_number, destination, seat_number, train_class) values (?, ?, ?, ?, ?)',
                 [request.form['name'], request.form['id_number'], request.form['destination'],
                  request.form['seat_number'], request.form['train_class']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login(): # ако има възможност за купуване online, друг username и password?
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Inavalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
        return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))
