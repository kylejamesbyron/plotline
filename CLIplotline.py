import os
import datetime
from datetime import datetime
from datetime import date
from datetime import time 
from flask import redirect
import time
import sqlite3

# End of opening

os.system('clear')
print('Welcome to PlotLine Setup') 
print()
time.sleep(3)

connection = sqlite3.connect('projdbs/erotic.db')
cursor = connection.cursor()
newbeat = '-' + input("Beat:")
cursor.execute("INSERT into SCENE (BEATS) VALUES (?)", (newbeat,))
connection.commit()
beats = cursor.execute('SELECT from SCENE (BEATS) VALUES (*)')
print(beats)




print(connection.total_changes)
