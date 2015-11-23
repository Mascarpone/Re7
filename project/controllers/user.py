# -*- coding: utf-8 -*-
from project import app, login_manager, gallery
from flask import g, render_template, request, redirect, url_for, abort, flash
from project.model.default import model
from project.model.user import User
from project.model.forms import RegisterForm, LoginForm
from flask.ext.login import login_user, logout_user, login_required

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
            flash('You have registered the username {0}. Please login'.format(login))
            return redirect(url_for('login'))
        else:
            flash('The username {0} is already in use. Please try a new username.'.format(login))
            return redirect(url_for('register'))

    return render_template('register.html', form = form)

@app.route('/user/<int:id>')
def user(id):
    user = model.getUserById(id)
    if user is not None:
        recipes = model.getRecipesByUserID(id)
        priceAvg = model.getUserPriceAvg(id)

        images = {}
        for recipe in recipes:
            image = gallery.url(recipe['image'])
            if not recipe['image']:
                image += 'recipe.png'
            images[recipe['recipeID']] = image

        return render_template('user.html', user=user, recipes=recipes, priceAvg=priceAvg, images=images)

    return abort(404)
