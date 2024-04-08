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


app = Flask(__name__)
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
	print()
	print(KEY)
	print(title)
	print()
	site = 'editscene/' + str(KEY)
	return redirect(site)

# Edit Scene
@app.route('/editscene/<KEY>')
def editscene(KEY):
	key = KEY
	import sqlite3
	connection = sqlite3.connect('projdbs/erotic.db')
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM MAIN WHERE KEY = ?", (key,))
	rows = cursor.fetchall()
	return render_template('editscene.html', rows=rows, key=key)
@app.route('/updatescene/<key>', methods = ['POST'])
def updatescene(key):
	title = request.form['TITLE']
	location = request.form['LOCATION']
	chapter = request.form['CHAPTER']
	scene = request.form['SCENE']
	tags = request.form['TAGS']

	import sqlite3
	connection = sqlite3.connect('projdbs/erotic.db')
	cursor = connection.cursor()
	cursor.execute('UPDATE MAIN SET TITLE = ?, LOCATION = ?, CHAPTER = ?, SCENE = ?, TAGS = ? WHERE KEY = ?', (title, location, chapter, scene, tags, key))
	connection.commit()

	site = '/editscene/' + str(key)

	return redirect(site)
	



# Close Flask
if __name__ == '__main__':
   app.run(debug = True)
