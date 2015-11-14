# -*- coding: utf-8 -*-
from project import app
from flask import render_template, redirect, url_for, flash
from project.model.default import model
from project.model.forms import RecipeForm

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
        return render_template('recipe.html', recipe=recipe, steps=steps)

    return redirect(url_for('index'))


@app.route('/recipes/create', methods=('GET', 'POST'))
def createRecipe():
    form = RecipeForm()

    if form.validate_on_submit():
        recipeID = model.insertRecipe(form.recipeName.data, form.budget.data,
                            form.difficulty.data, form.preparationTime.data,
                            form.cookingTime.data, 1, form.categoryID.data)
        i = 1;
        for step in form.steps.data:
            model.insertStep(i, step, recipeID)
            i += 1;

        return redirect(url_for('recipes'))
    return render_template('createRecipe.html', form=form)
