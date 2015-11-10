# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mysql import MySQL

app = Flask('project')
app.debug = True
app.secret_key = 'd0ntW4tch'

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'toor'
app.config['MYSQL_DATABASE_DB'] = 're7'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


from project.controllers import *
