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

# Home
@app.route('/')
def home():
   return render_template('home.html')


# Close Flask
if __name__ == '__main__':
   app.run(debug = True)