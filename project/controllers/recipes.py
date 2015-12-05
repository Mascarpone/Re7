# -*- coding: utf-8 -*-
from project import app, gallery
from flask import request, render_template, redirect, url_for, abort, flash, jsonify
from project.model.default import model
from project.model.forms import RecipeForm, CommentForm, ContainForm, SearchForm
from wtforms import FormField, TextAreaField, FieldList, validators
from flask.ext.login import current_user, login_required
from werkzeug import secure_filename
from flask.ext.uploads import UploadNotAllowed

@app.route('/recipes', methods=('GET', 'POST'))
@app.route('/recipes/<int:category>', methods=('GET', 'POST'))
def recipes(category=None):
    max = model.getMaxBudget()
    max = int(max['MAX(budget)'])
    min = model.getMinBudget()
    min = int(min['MIN(budget)'])
    form = SearchForm(csrf_enabled=False)
    if category is not None:
        form.categories.data = [category]
    recipes = model.getRecipesSearch(form.data['minprice'], form.data['maxprice'],
            form.data['ingredients'], form.data['categories'], form.data['query'])
    images = {}
    averages = {}
    for recipe in recipes:
        image = gallery.url(recipe['image'])
        if not recipe['image']:
            image += 'recipe.png'
        images[recipe['recipeID']] = image
        averages[recipe['recipeID']] = model.getAverageByRecipeID(recipe['recipeID'])

    return render_template('recipes.html', form=form, recipes=recipes, images=images, averages=averages, max=max, min=min)


@app.route('/recipes/<int:id>', methods=('GET', 'POST'))
def recipe(id):
    recipe = model.getRecipe(id)
    if recipe is not None:
        form = CommentForm()
        if form.validate_on_submit():
            if current_user.is_authenticated:
                comment = model.getCommentsByRecipeIDAndUserID(id, current_user.get_id())
                if comment is None:
                    model.insertComment(form.comment.data, form.tasteScore.data,
                        form.priceScore.data, form.instructionScore.data,
                         current_user.get_id(), id)
                else:
                    flash(u"Vous avez déjà commenté cette recette")

                return redirect(url_for('recipe', id=id))
            else :
                flash(u"Connectez-vous pour pouvoir commenter les recettes")
                return redirect(url_for('login'))

        steps = model.getStepsByRecipeID(id)
        image = gallery.url(recipe['image'])
        ingredients = model.getContainsByRecipeID(id)
        comments = model.getCommentsByRecipeID(id)
        averages = model.getAverageByRecipeID(id)

        if not recipe['image']:
            image += 'recipe.png'

        return render_template('recipe.html', recipe=recipe, steps=steps, image=image,
            ingredients=ingredients, form=form, comments=comments, averages=averages)

    return abort(404)


@app.route('/recipes/create', methods=('GET', 'POST'))
@login_required
def createRecipe():
    form = RecipeForm(csrf_enabled=False)
    ingredients = [i['ingredientName'] for i in model.getIngredients()]
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


        for contain in form.contains.data:
            ingredient = model.getIngredientByName(contain['ingredientName'])
            if ingredient is not None:
                ingredientID = ingredient['ingredientID']
            else:
                ingredientID = model.insertIngredient(contain['ingredientName'])

            model.insertContain(recipeID, ingredientID,
                    contain['quantity'], contain['isMain'],
                    contain['unitID'] )

        i = 1;
        print form.steps.data
        for step in form.steps.data:
            print step
            model.insertStep(i, step, recipeID)
            i += 1;

        return redirect(url_for('recipe', id=recipeID))
    return render_template('createRecipe.html', form=form, ingredients=ingredients)


@app.route('/recipes/edit/<int:id>', methods=('GET', 'POST'))
@login_required
def editRecipe(id):
    recipe = model.getRecipe(id)
    if recipe is not None:
        if recipe['userID'] == int(current_user.get_id()):
            ingredients = [i['ingredientName'] for i in model.getIngredients()]
            form = RecipeForm(csrf_enabled=False)

            if form.validate_on_submit():
                model.updateRecipe(id, form.recipeName.data, form.budget.data,
                    form.difficulty.data, form.preparationTime.data,
                    form.cookingTime.data, form.categoryID.data)

                return redirect(url_for('recipe', id=id))


            steps = model.getStepsByRecipeID(id)
            image = gallery.url(recipe['image'])
            contains = model.getContainsByRecipeID(id)
            comments = model.getCommentsByRecipeID(id)
            averages = model.getAverageByRecipeID(id)


            form.recipeName.data = recipe['recipeName']
            form.budget.data = recipe['budget']
            form.difficulty.data = recipe['difficulty']
            form.preparationTime.data = recipe['preparationTime']
            form.cookingTime.data = recipe['cookingTime']
            form.categoryID.data = recipe['categoryID']
            form.contains.pop_entry()

            for contain in contains:
                containform = ContainForm()
                containform.isMain = contain['isMain']
                containform.quantity = int(contain['quantity'])
                containform.unitID = contain['unitID']
                containform.ingredientName = contain['ingredientName']
                form.contains.append_entry(containform)

            for step in steps:
                form.steps.append_entry(step['stepDescription'])




            return render_template('editRecipe.html', form=form, ingredients=ingredients, id=id)


    return abort(404)


@app.route('/recipes/delete/<int:id>')
@login_required
def deleteRecipe(id):
    recipe = model.getRecipe(id)
    if recipe is not None:
        if recipe['userID'] == int(current_user.get_id()):

            if model.deleteRecipe(id) :
                flash(u'La recette {} a bien été supprimée.'.format(recipe['recipeName']))
            else:
                flash(u"La recette {} n'a pas pu être supprimée.".format(recipe['recipeName']))

            return redirect(url_for('manage'))

    return abort(404)
