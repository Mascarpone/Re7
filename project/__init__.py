# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask.ext.mysql import MySQL
from flask.ext.login import LoginManager
from flask.ext.uploads import UploadSet, IMAGES, configure_uploads

app = Flask('project')
app.debug = True
app.secret_key = 'd0ntW4tch'

# gallery configurations
app.config['UPLOADED_GALLERY_DEST'] = os.path.join(os.path.dirname(__file__), 'static', 'gallery')
gallery = UploadSet('gallery', IMAGES)
configure_uploads(app, gallery)

# login configurations
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = u'Veuillez vous connecter pour accéder à cette page.'

# MySQL configurations
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 're7'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)


from project.controllers import *
