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
    categories = model.getCategories()

    categoriesCount = {}
    for cat in categories:
        categoriesCount[cat['categoryID']] = model.getCategoryCountById(cat['categoryID'])

    recipes = {}
    for cat in categories:
        recipes[cat['categoryID']] = model.getBestRecipeByCategoryId(cat['categoryID'])

    images = {}
    for cat in categories:
        if recipes[cat['categoryID']] is None:
            image = 'recipe.png'
        else:
            image = gallery.url(recipes[cat['categoryID']]['image'])
            if not recipes[cat['categoryID']]['image']:
                image += 'recipe.png'
        images[cat['categoryID']] = image

    return render_template("index.html", categories=categories, categoriesCount=categoriesCount, recipes=recipes, images=images)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/ranking')
@app.route('/ranking/<int:id>')
def ranking(id=4):
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
