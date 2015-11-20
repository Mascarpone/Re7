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

    images = {}
    for recipe in recipes:
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        images[recipe['recipeID']] = image

    return render_template('recipes.html', recipes=recipes, ingredients=ingredients, categories=categories, images=images)
    pass

@app.route('/recipes/recipe/<int:id>')
def recipe(id):
    recipe = model.getRecipe(id)
    if recipe is not None:
        steps = model.getStepsByRecipeID(id)
        image = gallery.url(recipe['image'])
        ingredients = model.getContainsByRecipeID(id)
        if not recipe['image']:
            image += 'recipe.png'
        return render_template('recipe.html', recipe=recipe, steps=steps, image=image, ingredients=ingredients)

    return abort(404)



@app.route('/recipes/create', methods=('GET', 'POST'))
@login_required
def createRecipe():
    form = RecipeForm(csrf_enabled=False)
    if form.validate_on_submit():
        if form.image.data.filename:
            try:
                filename = gallery.save(form.image.data)
            except UploadNotAllowed:
                flash(u"Le format d'image n'est pas autorisé.")
        else:
            filename = ''

        recipeID = model.insertRecipe(form.recipeName.data, filename,
                    form.budget.data, form.difficulty.data,
                    form.preparationTime.data, form.cookingTime.data,
                    current_user.get_id(), form.categoryID.data)
        i = 1;
        for step in form.steps.data:
            model.insertStep(i, step, recipeID)
            i += 1;

        for ingredient in form.ingredients.data:
            model.insertContain(recipeID, ingredient['ingredientID'],
                    ingredient['quantity'], ingredient['isMain'],
                    ingredient['unitID'] )


        return redirect(url_for('recipes'))
    return render_template('createRecipe.html', form=form)
