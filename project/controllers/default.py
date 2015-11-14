# -*- coding: utf-8 -*-
from project import app
from flask import render_template, redirect, url_for
from project.model.default import model
from project.model.forms import RecipeForm


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

@app.route('/recipes')
def recipes():
    recipes = model.getRecipes()
    ingredients = model.getIngredients()
    return render_template('recipes.html', recipes=recipes, ingredients=ingredients)
    pass

@app.route('/recipe/<id>')
def recipe(id):
    recipe = model.getRecipe(id)
    return render_template('recipe.html', recipe=recipe)


@app.route('/createRecipe', methods=('GET', 'POST'))
def createRecipe():
    form = RecipeForm()

    if form.validate_on_submit():
        assert False
        model.insertRecipe(form.recipeName.data, form.budget.data,
                            form.difficulty.data, form.preparationTime.data,
                            form.cookingTime.data, 1, form.categoryID.data)
        return redirect(url_for('recipes'))
    return render_template('createRecipe.html', form=form)
