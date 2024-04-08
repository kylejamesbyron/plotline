from flask import Flask
from flask import send_file
from flask import render_template
from flask import request
import os
from flask import session
import datetime
from datetime import datetime
from datetime import date
from datetime import time 
from flask import redirect
import time
import sqlite3
# import pandas as pd


app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'
# End of opening

# Home Site
@app.route('/')
def home():
	return "Success"

# Create Scene
@app.route('/createscene')
def createscene():
	return render_template('createscene.html')

@app.route('/savescene', methods=['POST'])
def savescene():
	#Collect Requests
	title = request.form['TITLE']
	location = request.form['LOCATION']
	chapter = request.form['CH#']
	scene = request.form['SC#']
	tags = request.form['TAGS']

	#Write to DB
	connection = sqlite3.connect('projdbs/erotic.db')
	#connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("INSERT into MAIN (TITLE, LOCATION, CHAPTER, SCENE, TAGS) VALUES (?, ?, ?, ?, ?)", (title, location, chapter,scene, tags,))
	connection.commit()
	cursor.execute('SELECT KEY FROM MAIN WHERE TITLE = ?', (title,))
	KEY = cursor.fetchone()[0]
	site = 'editscene/' + str(KEY)
	scenenumber = 'scene' + str(KEY)
	cursor.execute('ALTER TABLE SCENE ADD COLUMN {} TEXT'.format(scenenumber),)
	connection.commit()
	return redirect(site)

# Edit Scene
@app.route('/editscene/<KEY>')
def editscene(KEY):
	key = str(KEY)
	scenenumber = 'scene' + str(KEY)
	import sqlite3
	connection = sqlite3.connect('projdbs/erotic.db')
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM MAIN WHERE KEY = ?", (key,))
	rows = cursor.fetchall()
	#maybe move the following line
	cursor.execute('SELECT * FROM SCENE WHERE ? != "NULL"', (scenenumber,))
	beat = cursor.fetchall()
	return render_template('editscene.html', rows=rows, key=key, beat=beat, scenenumber=scenenumber)
@app.route('/updatescene/<key>', methods = ['POST'])
def updatescene(key):
	scenenumber = 'scene' + str(key)
	title = request.form['TITLE']
	location = request.form['LOCATION']
	chapter = request.form['CHAPTER']
	scene = request.form['SCENE']
	tags = request.form['TAGS']
	beats = request.form['BEATS']

	import sqlite3
	connection = sqlite3.connect('projdbs/erotic.db')
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM SCENE WHERE "&scenenumber" IS NOT NULL')
	beat = cursor.fetchall()
	cursor.execute('UPDATE MAIN SET TITLE = ?, LOCATION = ?, CHAPTER = ?, SCENE = ?, TAGS = ? WHERE KEY = ?', (title, location, chapter, scene, tags, key))
	connection.commit()
	cursor.execute('INSERT into SCENE ({}) VALUES (?)'.format(scenenumber), (beats,))
	connection.commit()

	site = '/editscene/' + str(key)

	return redirect(site)

	#View Story

@app.route('/viewoutline')
def viewoutline():

	
	import sqlite3
	connection = sqlite3.connect('projdbs/erotic.db')
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM MAIN WHERE TITLE is not NULL')
	info = cursor.fetchall()
	print(str(info))
	for row in info:
		print(row["TITLE"])
		print(row["KEY"])
		key = row['KEY']
	scenenumber = 'scene' + str(key)
	print(scenenumber)
	cursor.execute('SELECT * FROM SCENE WHERE ? != "NULL"', (scenenumber,))
	beat = cursor.fetchall()

	return render_template('viewoutline.html', info=info, beat=beat, scenenumber=scenenumber, key=key)



# Close Flask
if __name__ == '__main__':
   app.run(debug = True)
