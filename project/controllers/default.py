# -*- coding: utf-8 -*-
from project import app
from flask import render_template, request, redirect, url_for
from project.model.default import model
from flask.ext.wtf import Form
from wtforms import SelectField, TextField, IntegerField, validators

class RecipeForm(Form):
    recipeName = TextField(u'Nom de la recette', [validators.Required()])
    budget = IntegerField(u'Budget', [validators.Required()])
    difficulty = IntegerField(u'Difficulté', [validators.Required(), validators.NumberRange(min=1, max=5)])
    preparationTime = IntegerField(u'Temps de préparation', [validators.Required()])
    cookingTime = IntegerField(u'Temps de cuisson', [validators.Required()])
    categoryID = SelectField(u'Type de plat', choices = [a.values() for a in model.getCategories()],
        coerce=int, validators=[validators.Required()])

@app.context_processor
def config_template():
    return dict(template = "alternate.html")

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
    recipes = model.getRecipes()
    return render_template('recipes.html', recipes=recipes)
    pass

@app.route('/recipe/<id>')
def recipe(id):
    recipe = model.getRecipe(id)
    return render_template('recipe.html', recipe=recipe)


@app.route('/createRecipe', methods=('GET', 'POST'))
def createRecipe():
    form = RecipeForm()
    if form.validate_on_submit():
        model.insertRecipe(form.recipeName.data, form.budget.data,
                            form.difficulty.data, form.preparationTime.data,
                            form.cookingTime.data, 1, form.categoryID.data)
        return redirect(url_for('recipes'))
    return render_template('createRecipe.html', form=form)
