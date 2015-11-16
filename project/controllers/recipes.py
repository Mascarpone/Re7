# -*- coding: utf-8 -*-
from project import app, gallery
from flask import render_template, redirect, url_for, flash
from project.model.default import model
from project.model.forms import RecipeForm
from flask.ext.login import current_user, login_required
from werkzeug import secure_filename
from flask.ext.uploads import UploadNotAllowed

@app.route('/recipes')
def recipes():
    recipes = model.getRecipes()
    ingredients = model.getIngredients()
    categories = model.getCategories()
    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, categories=categories)
    pass

@app.route('/recipes/recipe/<int:id>')
def recipe(id):
    recipe = model.getRecipe(id)
    if recipe is not None:
        steps = model.getStepsByRecipeID(id)
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        return render_template('recipe.html', recipe=recipe, steps=steps, image=image)

    return abort(404)



@app.route('/recipes/create', methods=('GET', 'POST'))
@login_required
def createRecipe():
    form = RecipeForm()
    #csrf
    assert False
    if form.validate_on_submit():
        assert False
        try:
            filename = gallery.save(form.image.data)
        except UploadNotAllowed:
            flash("Le format d'image n'est pas authorisé.")
        else:
            recipeID = model.insertRecipe(form.recipeName.data, filename, form.budget.data,
                        form.difficulty.data, form.preparationTime.data,
                        form.cookingTime.data, current_user.get_id(), form.categoryID.data)
            i = 1;
            for step in form.steps.data:
                model.insertStep(i, step, recipeID)
                i += 1;

        return redirect(url_for('recipes'))
    return render_template('createRecipe.html', form=form)
