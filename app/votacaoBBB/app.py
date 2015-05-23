# coding=utf-8

# Imports
import sqlite3
import datetime
import json
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
from flask_recaptcha import ReCaptcha

# Create Application
app = Flask(__name__)
app.config.from_envvar('VOTACAOBBB_SETTINGS', silent=True)
recaptcha = ReCaptcha(app)

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

def query_db(query, args=(), one=False):
	cur = get_db().execute(query, args)
	rv = cur.fetchall()
	cur.close()
	return (rv[0] if rv else None) if one else rv

# Convert a list to a dictionary
def list_to_dic(list):
	my_dict = {}
	index = 0
	for item in list:
		my_dict[index] = item
		index+=1
	return my_dict


@app.before_request
def before_request():
	g.db = connect_db()

@app.teardown_appcontext
def close_connection(exception):
	if hasattr(g, 'sqlite3_db'):
		db = getattr(g, 'sqlite_db')
		if db is not None:
			db.close()

# Update History
def update_history(participant_id):
	actual_hour = datetime.datetime.now().strftime('%Y%m%d%H')
	id_hora = query_db('select id from hour_votings where date_hour = ? and participant_id = ?',
		[actual_hour, participant_id])
	if id_hora is not None:
		get_db().execute('update hour_votings set votes = votes + 1 where date_hour = ? and participant_id = ?',
			[actual_hour, participant_id])
	else:
		get_db().execute('insert into hour_votings (date_hour, participant_id, votes) values(?, ?, 1)',
			[actual_hour, participant_id])


# Home
@app.route('/')
def home():
	return render_template('main.html')

# Voting
@app.route('/vote/<int:participant_id>', methods = [ 'GET', 'POST'])
def vote(participant_id):
	# Verify valid ID
	if participant_id not in range(1,3):
		flash("Escolha um participante")
		return render_template('main.html')
	elif not recaptcha.verify():
		flash(u"Confirme que você é um humano!")
		return render_template('main.html')
	else:
		#Update votes and history
		get_db().execute('update participants set votes = votes + 1 where id = ?',
			[participant_id])
		update_history(participant_id)
		get_db().commit()
		entries = query_db('select * from participants')
		if request.method == 'GET':
			return jsonify(list_to_dic(entries))
		else:
			return render_template('result.html', entries = entries, participant_name = entries[participant_id-1]['name'] )

# Just show the Results
@app.route('/results')
def results():
	entries = query_db('select * from participants')
	return render_template('result.html', entries = entries)


# Start Server
if __name__ == '__main__':
	app.run()
