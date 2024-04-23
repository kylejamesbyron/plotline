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

# Settings List
settings = [('narrative',),
            ('projectname',),
            ('database',),
            ('logline',),]

# Home
@app.route('/')
def home():
   return render_template('home.html')
   
# New Project
@app.route('/createdb', methods=['post'])
def createdb():
   projectname = request.form['projectname']
   project_name = projectname.replace(" ", "_")
   session['database'] = 'projdbs/' + project_name + '.db'
   database = session.get('database')
   open(database, 'x')
   connection = sqlite3.connect(database)
   cursor = connection.cursor()
   cursor.execute("CREATE TABLE settings (KEY INTEGER UNIQUE,\
                   VARIABLE TEXT UNIQUE, SETTING TEXT, NNUMBER INTEGER,\
                   PRIMARY KEY('KEY' AUTOINCREMENT))")
   connection.commit()
   cursor.executemany("INSERT INTO settings (VARIABLE) VALUES (?)", (settings))
   connection.commit()
   cursor.execute("UPDATE settings SET NNUMBER = ? WHERE VARIABLE == ?",\
                   (0, 'narrative'))
   connection.commit()
   cursor.execute("CREATE TABLE MAIN (KEY INTEGER UNIQUE, CHAPTER INTEGER, SCENE INTEGER, TITLE TEXT UNIQUE, LOCATION TEXT, TAGS TEXT, PRIMARY KEY('KEY'))")
   connection.commit()
   cursor.execute("CREATE TABLE SCENE (BEAT INTEGER, KEY INTEGER, NARRATIVE TEXT, PRIMARY KEY('BEAT' AUTOINCREMENT))")
   connection.commit()
   

   site = '/newproject/' + project_name
   return redirect(site)

@app.route('/newproject/<project_name>')
def newproject(project_name):
   projectname = project_name.replace("_", " ")
   database = 'projdbs/' + project_name + '.db'
   return render_template('newproject.html',\
                           projectname=projectname, project_name=project_name,\
                          database=database)

@app.route('/savesettings', methods=['post'])
def savesettings():
   session['projectname'] = request.form['projectname']
   projectname = session.get('projectname')
   session['database'] = request.form['database']
   database = session.get('database')
   session['logline'] = request.form['logline']
   logline = session.get('logline')
   connection = sqlite3.connect(database)
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT VARIABLE FROM settings WHERE KEY is not NULL")
   variables = cursor.fetchall()
   for variable in variables:
      if variable['VARIABLE'] == 'projectname':
         update = projectname
         projectname = update
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?",\
                         (update, variable['VARIABLE'],))
         connection.commit()
      elif variable['VARIABLE'] == 'logline':
         update = logline
         logline = update
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?",\
                         (update, variable['VARIABLE'],))
         connection.commit()
      elif variable['VARIABLE'] == 'database':
         update = database
         database = update
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?",\
                         (update, variable['VARIABLE'],))
         connection.commit()

    
   cursor.execute("SELECT * FROM settings WHERE KEY is not NULL") 
   narratives = cursor.fetchall() 
   for narrative in narratives:
      if narrative['VARIABLE'].startswith('narrative'):
         NNUMBER = narrative['NNUMBER']
         nnumberstr = str(NNUMBER)
         
   return render_template('newnarratives.html', projectname=projectname,\
    logline=logline, database=database, narratives=narratives,\
        nnumberstr=nnumberstr, NNUMBER=NNUMBER)


# Save Narrative
@app.route('/savenarrative', methods=['post'])
def savenarrative():
   projectname = session.get('projectname')
   #database = request.form['database']
   database = session.get('database')
   logline = session.get('logline')
   newnarrative = request.form['newnarrative']
   newnarrativenumber = request.form['newnarrativenumber']
   newnarrativename = 'narrative' + str(newnarrativenumber)
   connection = sqlite3.connect(database)
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("INSERT INTO settings (VARIABLE, SETTING, NNUMBER)\
                   VALUES (?, ?, ?)", (newnarrativename, newnarrative,\
                                        newnarrativenumber))
   connection.commit()
   cursor.execute("SELECT * FROM settings WHERE KEY is not NULL") 
   narratives = cursor.fetchall() 
   for narrative in narratives:
      if narrative['VARIABLE'].startswith('narrative'):
         NNUMBER = narrative['NNUMBER']
         nnumberstr = str(NNUMBER)
#Create Config
         if narrative['VARIABLE'].endswith('narrative1'):
            narrative = narrative['SETTING']
            session['narrative1'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative2':
            narrative = narrative['SETTING']
            session['narrative2'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative3':
            narrative = narrative['SETTING']
            session['narrative3'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative4':
            narrative = narrative['SETTING']
            session['narrative4'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative5':
            narrative = narrative['SETTING']
            session['narrative5'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative6':
            narrative = narrative['SETTING']
            session['narrative6'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative7':
            narrative = narrative['SETTING']
            session['narrative7'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative8':
            narrative = narrative['SETTING']
            session['narrative8'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative9':
            narrative = narrative['SETTING']
            session['narrative9'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative10':
            narrative = narrative['SETTING']
            session['narrative10'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative11':
            narrative = narrative['SETTING']
            session['narrative11'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative12':
            narrative = narrative['SETTING']
            session['narrative12'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative13':
            narrative = narrative['SETTING']
            session['narrative13'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative14':
            narrative = narrative['SETTING']
            session['narrative14'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative15':
            narrative = narrative['SETTING']
            session['narrative15'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative16':
            narrative = narrative['SETTING']
            session['narrative16'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative17':
            narrative = narrative['SETTING']
            session['narrative17'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative18':
            narrative = narrative['SETTING']
            session['narrative18'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative19':
            narrative = narrative['SETTING']
            session['narrative19'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative20':
            narrative = narrative['SETTING']
            session['narrative20'] = str(narrative)
         
 #  return session.get('narrative1')
   return render_template('createnarratives.html', projectname=projectname,\
                          logline=logline, database=database, \
                           narratives=narratives, nnumberstr=nnumberstr,\
                                NNUMBER=NNUMBER)

# Open Project
@app.route('/openproject')
def openproject():
   files = os.listdir('/home/maisom/Documents/GitHub/plotline/projdbs')
   return render_template('openproject.html', files=files)
@app.route('/chooseproject', methods=['post'])
def chooseproject():
   database = request.form["openproject"]
   session['database'] = 'projdbs/' + database
   connection = sqlite3.connect(session['database'])
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM settings where KEY is not null")
   narratives = cursor.fetchall()
   for narrative in narratives:
      if narrative['VARIABLE'].startswith('narrative'):
         NNUMBER = narrative['NNUMBER']
         nnumberstr = str(NNUMBER)
#Create Config
         if narrative['VARIABLE'].endswith('narrative1'):
            narrative = narrative['SETTING']
            session['narrative1'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative2':
            narrative = narrative['SETTING']
            session['narrative2'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative3':
            narrative = narrative['SETTING']
            session['narrative3'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative4':
            narrative = narrative['SETTING']
            session['narrative4'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative5':
            narrative = narrative['SETTING']
            session['narrative5'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative6':
            narrative = narrative['SETTING']
            session['narrative6'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative7':
            narrative = narrative['SETTING']
            session['narrative7'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative8':
            narrative = narrative['SETTING']
            session['narrative8'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative9':
            narrative = narrative['SETTING']
            session['narrative9'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative10':
            narrative = narrative['SETTING']
            session['narrative10'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative11':
            narrative = narrative['SETTING']
            session['narrative11'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative12':
            narrative = narrative['SETTING']
            session['narrative12'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative13':
            narrative = narrative['SETTING']
            session['narrative13'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative14':
            narrative = narrative['SETTING']
            session['narrative14'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative15':
            narrative = narrative['SETTING']
            session['narrative15'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative16':
            narrative = narrative['SETTING']
            session['narrative16'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative17':
            narrative = narrative['SETTING']
            session['narrative17'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative18':
            narrative = narrative['SETTING']
            session['narrative18'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative19':
            narrative = narrative['SETTING']
            session['narrative19'] = str(narrative)
         elif narrative['VARIABLE'] == 'narrative20':
            narrative = narrative['SETTING']
            session['narrative20'] = str(narrative)
   return redirect('/viewoutline')


# START PLOTLINE PROPER
     

# Create Scene
@app.route('/createscene')
def createscene():
    database = session.get('database')
	#connection = sqlite3.connect('projdbs/' +database)
    connection = sqlite3.connect(database)
    cursor = connection.cursor()
    cursor.execute("INSERT or REPLACE into MAIN (CHAPTER, SCENE, TITLE) VALUES (1, 0, 'blank')")
    connection.commit()
    cursor.execute('SELECT SCENE FROM MAIN order by CHAPTER, SCENE DESC LIMIT 1')
    [scenenumber] = cursor.fetchone()
    scenenumberint = str(scenenumber)
    cursor.execute('SELECT CHAPTER FROM MAIN order by CHAPTER, SCENE DESC LIMIT 1')
    [chapternumber] = cursor.fetchone()
    return render_template('createscene.html', scenenumber=scenenumber, chapternumber=chapternumber)
    #return scenenumberint

@app.route('/savescene', methods=['post'])
def savescene():
   #Collect Requests
   title = request.form['TITLE']
   location = request.form['LOCATION']
   chapter = request.form['CH#']
   scene = request.form['SC#']
   tags = request.form['TAGS']

	#Write to DB
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT SCENE FROM main")
   scenelist = cursor.fetchall()
   for oldscene in scenelist:
      if oldscene['SCENE'] == int(scene):
         cursor.execute("UPDATE main SET scene = scene + 1 WHERE scene >= ?", (scene))
   
      

   cursor.execute("INSERT into MAIN (TITLE, LOCATION, CHAPTER, SCENE, TAGS) \
		VALUES (?, ?, ?, ?, ?)", (title, location, chapter, scene, tags,))
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
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM MAIN WHERE KEY = ?", (key,))
   rows = cursor.fetchall()
   #maybe move the following line
   cursor.execute('SELECT * FROM SCENE WHERE ? != "NULL"', (scenenumber,))
   beat = cursor.fetchall()
   narrative1 = session.get('narrative1')
   narrative2 = session.get('narrative2')
   narrative3 = session.get('narrative3')
   narrative4 = session.get('narrative4')
   narrative5 = session.get('narrative5')
   narrative6 = session.get('narrative6')
   narrative7 = session.get('narrative7')
   narrative8 = session.get('narrative8')
   narrative9 = session.get('narrative9')
   narrative10 = session.get('narrative10')
   narrative11 = session.get('narrative11')
   narrative12 = session.get('narrative12')
   narrative13 = session.get('narrative13')
   narrative14 = session.get('narrative14')
   narrative15 = session.get('narrative15')
   narrative16 = session.get('narrative16')
   narrative17 = session.get('narrative17')
   narrative18 = session.get('narrative18')
   narrative19 = session.get('narrative19')
   narrative20 = session.get('narrative20')
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
	connection = sqlite3.connect(session.get('database'))
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
   narrative1 = session.get('narrative1')
   narrative2 = session.get('narrative2')
   narrative3 = session.get('narrative3')
   narrative4 = session.get('narrative4')
   narrative5 = session.get('narrative5')
   narrative6 = session.get('narrative6')
   narrative7 = session.get('narrative7')
   narrative8 = session.get('narrative8')
   narrative9 = session.get('narrative9')
   narrative10 = session.get('narrative10')
   narrative11 = session.get('narrative11')
   narrative12 = session.get('narrative12')
   narrative13 = session.get('narrative13')
   narrative14 = session.get('narrative14')
   narrative15 = session.get('narrative15')
   narrative16 = session.get('narrative16')
   narrative17 = session.get('narrative17')
   narrative18 = session.get('narrative18')
   narrative19 = session.get('narrative19')
   narrative20 = session.get('narrative20')
   import sqlite3
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   # Get scene info
   cursor.execute('SELECT * FROM MAIN WHERE TITLE is not NULL ORDER BY\
    CHAPTER, SCENE' )
   info = cursor.fetchall()
   # Get scene beats
   cursor.execute('SELECT * FROM SCENE WHERE KEY != "NULL"')
   beats = cursor.fetchall()
   return render_template('viewoutline.html', info=info,\
   					   beats=beats, narrative1=narrative1, narrative2=narrative2,\
     narrative3=narrative3, narrative4=narrative4, narrative5=narrative5,\
     narrative6=narrative6, narrative7=narrative7, narrative8=narrative8,\
     narrative9=narrative9, narrative10=narrative10, narrative11=narrative11,\
     narrative12=narrative12, narrative13=narrative13, narrative14=narrative14,\
     narrative15=narrative15, narrative16=narrative16, narrative17=narrative17,\
     narrative18=narrative18, narrative19=narrative19, narrative20=narrative20)

#Edit Narratives
@app.route('/addnarrative')
def addnarratives():
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT NNUMBER FROM settings ORDER BY NNUMBER DESC LIMIT 1")
   nnumber = cursor.fetchone()
   return render_template('editnarrative.html', nnumber=nnumber)

@app.route('/editbeat/<SCENE>/<BEAT>')
def editbeat(SCENE, BEAT):
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT * FROM SCENE WHERE BEAT == ?", (BEAT)) 
   beat = cursor.fetchall()
   return render_template('editbeat.html', beat=beat, SCENE=SCENE)

@app.route('/savebeat/<SCENE>/<BEAT>', methods=['post', 'get'])
def savebeat(SCENE, BEAT):
   connection = sqlite3.connect(session.get('database'))
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   newbeat = request.form['newbeat']
   
   cursor.execute("UPDATE SCENE SET {} = ? WHERE BEAT == ?".format(SCENE), (newbeat, BEAT))
   connection.commit()
   return redirect('/viewoutline')

   

# Close Flask
if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0" )
