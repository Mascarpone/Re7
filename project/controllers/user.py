# -*- coding: utf-8 -*-
from project import app, login_manager, gallery
from flask import g, render_template, request, redirect, url_for, abort, flash
from project.model.default import model
from project.model.user import User
from project.model.forms import RegisterForm, LoginForm
from flask.ext.login import login_user, logout_user, login_required, current_user

@login_manager.user_loader
def user_loader(user_id):
    user = model.getUserById(user_id)
    if user is not None:
        g.user = User(user['userID'], user['login'], user['password'])
        return g.user
    return None

@app.route('/user/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/user/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        user = model.getUserByLoginAndPassword(login, password)
        if user is not None:
            g.user = User(user['userID'], user['login'], user['password'])
            login_user(g.user)
            flash('Bienvenue {0}'.format(login))
            return redirect(url_for('index'))
        else:
            flash('Invalid login')
            return redirect(url_for('login'))

    return render_template('login.html', form = form)

@app.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        login = form.login.data
        password = form.password.data

        user = model.getUserByLogin(login)
        if user is None:
            model.insertUser(login, password)
            flash('Vous vous etes enregistre avec le nom d utilisateur {0}. Veuillez vous connecter.'.format(login))
            return redirect(url_for('login'))
        else:
            flash('Le nom d utilisateur {0} est deja utilise. Veuillez choisir un autre nom.'.format(login))
            return redirect(url_for('register'))

    return render_template('register.html', form = form)

@app.route('/user/<int:id>')
def user(id):
    user = model.getUserById(id)
    if user is not None:
        recipes = model.getRecipesByUserID(id)
        priceAvg = model.getUserPriceAvg(id)

        images = {}
        averages = {}
        for recipe in recipes:
            image = gallery.url(recipe['image'])
            if not recipe['image']:
                image += 'recipe.png'
            images[recipe['recipeID']] = image

            averages[recipe['recipeID']] = model.getAverageByRecipeID(recipe['recipeID'])

        return render_template('user.html', user=user, recipes=recipes, priceAvg=priceAvg, images=images, averages=averages)

    return abort(404)

@app.route('/user/manage')
@login_required
def manage():
    recipes = model.getRecipesByUserID(current_user.get_id())
    return render_template('manage.html', recipes=recipes)
