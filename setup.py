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
settings = [#{'narrative1,'},
#           {'narrative2,'},
#           {'narrative3,'},
#           {'narrative4,'},
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
   database = 'projdbs/' + project_name + '.db'
   open(database, 'x')
   connection = sqlite3.connect(database)
   cursor = connection.cursor()
   cursor.execute("CREATE TABLE settings (KEY INTEGER UNIQUE, VARIABLE TEXT, SETTING TEXT,\
                   PRIMARY KEY('KEY' AUTOINCREMENT))")
   connection.commit()
   cursor.executemany("INSERT INTO settings (VARIABLE) VALUES (?)", (settings))
   connection.commit()
   
   site = '/newproject/' + project_name
   return redirect(site)

@app.route('/newproject/<project_name>')
def newproject(project_name):
   projectname = project_name.replace("_", " ")
   database = 'projdbs/' + project_name + '.db'
   return render_template('newproject.html', projectname=projectname, project_name=project_name,\
                          database=database)

@app.route('/savesettings', methods=['post'])
def savesettings():
   projectname = request.form['projectname']
   database = request.form['database']
   logline = request.form['logline']
   #narrative1 = request.form['narrative1']
   connection = sqlite3.connect(database)
   connection.row_factory = sqlite3.Row
   cursor = connection.cursor()
   cursor.execute("SELECT VARIABLE FROM settings WHERE KEY is not NULL")
   variables = cursor.fetchall()
   for variable in variables:
      if variable['VARIABLE'] == 'projectname':
         update = projectname
         projectname = update
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?", (update, variable['VARIABLE'],))
         connection.commit()
      elif variable['VARIABLE'] == 'logline':
         update = logline
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?", (update, variable['VARIABLE'],))
         connection.commit()
      elif variable['VARIABLE'] == 'databse':
         update = database
         cursor.execute("UPDATE settings SET SETTING = ? WHERE VARIABLE = ?", (update, variable['VARIABLE'],))
         connection.commit()   
   return projectname



# Close Flask
if __name__ == '__main__':
   app.run(debug = True)