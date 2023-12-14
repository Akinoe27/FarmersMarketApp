#call the flask object
from flask import Flask
from flask_mysqldb import MySQL

#create a new name for Flask
app = Flask(__name__)


#database credentials XAMPP
#hostname "localhost"
app.config['MYSQL_HOST'] = 'localhost'
#username "root"
app.config['MYSQL_USER'] = 'root'
#password "root"
app.config['MYSQL_PASSWORD'] = ''
#database
app.config['MYSQL_DB'] = 'marvin'

#initialize all XAMPP credentials
mysql = MySQL (app)





#call routes from the flask
from app import routes

