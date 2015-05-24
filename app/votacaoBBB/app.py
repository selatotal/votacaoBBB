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
	id_hora = query_db('select id from hour_votings where date_hour = ?',
		[actual_hour])

	if (participant_id == 1):
		participant1_votes = 1
		participant2_votes = 0
	elif (participant_id == 2):
		participant1_votes = 0
		participant2_votes = 1

	if not id_hora:
		get_db().execute('insert into hour_votings (date_hour, participant1_votes, participant2_votes) values(?, ?, ?)',
			[actual_hour, participant1_votes, participant2_votes])
	else:
		get_db().execute('update hour_votings set participant1_votes = participant1_votes + ?, participant2_votes = participant2_votes + ? where date_hour = ?',
			[participant1_votes, participant2_votes, actual_hour])


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

# Admin login form
@app.route('/admin')
def admin():
	return render_template('admin_index.html')

# Admin logout
@app.route('/admin/logout')
def admin_logout():
	session.pop('username', None)
	return redirect(url_for('admin'))

# Admin login e homepage
@app.route('/admin/home', methods = [ 'GET','POST' ])
def admin_home():
	if 'username' not in session:
		if (request.method == 'POST') and (request.form['username'] == app.config['USERNAME']) and (request.form['password'] == app.config['PASSWORD']):
			session['username'] = 'admin'
		else:
			session.pop('username', None)
			return render_template('admin_index.html')

	# Get logout data
	total_votes = query_db("select sum(votes) 'total' from participants")
	results = query_db("select id, name, votes, ((votes/?)*100.0) 'perc' from participants",
		[ total_votes[0]['total']*1.0 ] )
	by_hour = query_db('select * from hour_votings order by date_hour')
	return render_template('admin_home.html', total_votes = total_votes[0]['total'] , results = results, by_hour = by_hour)

# Start Server
if __name__ == '__main__':
	app.run(host = app.config['IP_BIND'], port = app.config['PORT'])
