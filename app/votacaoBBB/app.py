# Imports
import sqlite3
import datetime
import json
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify

# Create Application
app = Flask(__name__)
app.config.from_envvar('VOTACAOBBB_SETTINGS', silent=True)

# Connect Database
def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

def init_db():
	db = get_db()
	with app.open_resource('schema.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

def make_dicts(cursor, row):
	return dict((cursor.description[idx][0], value) for idx, value in enumerate(row))

def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = make_dicts
	return rv

def list_to_dic(list):
	my_dict = {}
	index = 0
	for item in list:
		my_dict[index] = item
		index+=1
	return my_dict

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv


@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_appcontext
def close_connection(exception):
	db = getattr(g, 'sqlite_db')
	if db is not None:
		db.close()

# Update History
def update_history(participant_id):
	actual_hour = datetime.datetime.now().strftime('%Y%m%d%H')
	id_hora = g.db.execute('select id from hour_votings where date_hour = ? and participant_id = ?',
		[actual_hour, participant_id])
	if id_hora is not None:
		g.db.execute('update hour_votings set votes = votes + 1 where date_hour = ? and participant_id = ?',
			[actual_hour, participant_id])
	else:
		g.db.execute('insert into hour_votings (date_hour, participant_id, votes) values(?, ?, 1)',
			[actual_hour, participant_id])


# Home
@app.route('/')
def home():
	return render_template('main.html')

# Voting
@app.route('/vote/<int:participant_id>')
def vote(participant_id):
	g.db.execute('update participants set votes = votes + 1 where id = ?',
		[participant_id])
	update_history(participant_id)
	g.db.commit()
	entries = query_db('select * from participants')	
	return jsonify(list_to_dic(entries));

# Results
@app.route('/results')
def results():
	entries = g.db.execute('select * from participants')
	return render_template('result.html', entries = entries)


# Start Server
if __name__ == '__main__':
	app.run()
