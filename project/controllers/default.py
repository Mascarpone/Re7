# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request
from project.model import model


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/recipes')
def recipes():
    #rcs = model.getRecipes()
    #return render_template('recipes.html', rcs=rcs)
    pass

@app.route('/recipe/<id>')
def recipe(id):
    #r = model.getRecipe(id)
    #return render_template('recipes.html', r=r)
    pass
