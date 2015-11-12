# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mysql import MySQL
from flask.ext.login import LoginManager

app = Flask('project')
app.debug = True
app.secret_key = 'd0ntW4tch'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
app.config['MYSQL_DATABASE_DB'] = 're7'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


from project.controllers import *
