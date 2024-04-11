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

#Config
database = 'erotic.db'
narrative1 = 'Prisoners'
narrative2 = 'Terrorism'
narrative3 = 'Liam + Sophia'
narrative4 = 'Emma is a spy'
narrative5 = 'Jean is Evil'
narrative6 = 'Elijah Investigates'
narrative7 = 'Emma is Dead'
narrative8 = 'Rachel + Ben'
narrative9 = 'Ben + Sophia'
narrative10 = 'Rachel needs Bens Help'
narrative11 = 'Sophia Investigates Repairs'
narrative12 = 'Liam Investigates Terrorism'
narrative13 = 'Jean + Sophia'
narrative14 = 'Emma + Jean'
narrative15 = 'The ONHR'
narrative16 = 'Special'
narrative17 = ''
narrative18 = ''
narrative19 = ''
narrative20 = ''


# Home Site
@app.route('/')
def home():
	return "Success"

# Create Scene
@app.route('/createscene')
def createscene():

	connection = sqlite3.connect('projdbs/' + database)
	cursor = connection.cursor()
	cursor.execute('SELECT SCENE FROM MAIN order by CHAPTER, SCENE DESC LIMIT 1')
	[scenenumber] = cursor.fetchone()
	cursor.execute('SELECT CHAPTER FROM MAIN order by CHAPTER, SCENE DESC LIMIT 1')
	[chapternumber] = cursor.fetchone()
	return render_template('createscene.html', scenenumber=scenenumber, chapternumber=chapternumber)

@app.route('/savescene', methods=['POST'])
def savescene():
	#Collect Requests
	title = request.form['TITLE']
	location = request.form['LOCATION']
	chapter = request.form['CH#']
	scene = request.form['SC#']
	tags = request.form['TAGS']

	#Write to DB
	connection = sqlite3.connect('projdbs/' + database)
	cursor = connection.cursor()
	cursor.execute("INSERT into MAIN (TITLE, LOCATION, CHAPTER, SCENE, TAGS) \
		VALUES (?, ?, ?, ?, ?)", (title, location, chapter,scene, tags,))
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
	connection = sqlite3.connect('projdbs/' + database)
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	cursor.execute("SELECT * FROM MAIN WHERE KEY = ?", (key,))
	rows = cursor.fetchall()
	#maybe move the following line
	cursor.execute('SELECT * FROM SCENE WHERE ? != "NULL"', (scenenumber,))
	beat = cursor.fetchall()
	return render_template('editscene.html', rows=rows, key=key, beat=beat,\
	 scenenumber=scenenumber, narrative1=narrative1, narrative2=narrative2,\
	  narrative3=narrative3, narrative4=narrative4, narrative5=narrative5,\
	  narrative6=narrative6, narrative7=narrative7, narrative8=narrative8,\
	  narrative9=narrative9, narrative10=narrative10, narrative11=narrative11,\
	  narrative12=narrative12, narrative13=narrative13, narrative14=narrative14,\
	  narrative15=narrative15, narrative16=narrative16, narrative17=narrative17,\
	  narrative18=narrative18, narrative19=narrative19, narrative20=narrative20)

@app.route('/updatescene/<key>', methods = ['POST'])
def updatescene(key):
	scenenumber = 'scene' + str(key)
	title = request.form['TITLE']
	location = request.form['LOCATION']
	chapter = request.form['CHAPTER']
	scene = request.form['SCENE']
	tags = request.form['TAGS']
	beats = request.form['BEATS']
	narrative = request.form['NARRATIVE']
	addtags = request.form['ADDTAGS']
	

	import sqlite3
	connection = sqlite3.connect('projdbs/' + database)
	cursor = connection.cursor()
	cursor.execute('UPDATE MAIN SET TITLE = ?, LOCATION = ?, CHAPTER = ?,\
	 SCENE = ?, TAGS = ? WHERE KEY = ?',\
	  (title, location, chapter, scene, tags, key))
	connection.commit()
	cursor.execute('INSERT into SCENE ({}, KEY, NARRATIVE) VALUES (?, ?, ?)'.format(scenenumber),\
	 (beats, key, narrative))
	connection.commit()
	
	site = '/editscene/' + str(key)
	return redirect(site)

#View Story

@app.route('/viewoutline')
def viewoutline():

	import sqlite3
	connection = sqlite3.connect('projdbs/' + database)
	connection.row_factory = sqlite3.Row
	cursor = connection.cursor()
	# Get scene info
	cursor.execute('SELECT * FROM MAIN WHERE TITLE is not NULL ORDER BY\
	 CHAPTER, SCENE' )
	info = cursor.fetchall()
	# Get scene beats
	cursor.execute('SELECT * FROM SCENE WHERE KEY != "NULL"')
	beats = cursor.fetchall()
	
	return render_template('viewoutline.html', info=info, beats=beats, narrative1=narrative1)



# Close Flask
if __name__ == '__main__':
   app.run(debug = True)
