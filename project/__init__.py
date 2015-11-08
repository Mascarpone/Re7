# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mysql import MySQL

app = Flask('project')
app.debug = True

mysql = MySQL()
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = ''
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#mysql.init_app(app)


from project.controllers import *
