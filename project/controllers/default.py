# -*- coding: utf-8 -*-
from project import app, gallery
from flask import render_template

from project.model.default import model

@app.context_processor
def config_template():
    return dict(template = "base.html")

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/ranking')
@app.route('/ranking/<int:id>')
def ranking(id=8):
    QP = model.getRanking_QP(id)
    FastDesserts = model.getRanking_FastDesserts(id)
    MostCommented = model.getRanking_MostCommented(id)

    images = {}
    for recipe in QP:
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        images[recipe['recipeID']] = image
    for recipe in FastDesserts:
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        images[recipe['recipeID']] = image
    for recipe in MostCommented:
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        images[recipe['recipeID']] = image

    return render_template("ranking.html", id=id, QP=QP, FastDesserts=FastDesserts, MostCommented=MostCommented, images=images)
