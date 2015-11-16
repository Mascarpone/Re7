# -*- coding: utf-8 -*-
from default import model
from flask.ext.wtf import Form
from wtforms import SelectField, TextField, IntegerField, FieldList, PasswordField, validators
from flask_wtf.file import FileField, FileAllowed
from project import gallery

class RecipeForm(Form):
    image = FileField('Image', [validators.optional(), FileAllowed(gallery, "Images only!")])
    recipeName = TextField(u'Nom de la recette', [validators.Required()])
    budget = IntegerField(u'Budget')
    difficulty = IntegerField(u'Difficulté', [validators.Required(), validators.NumberRange(min=1, max=5)])
    preparationTime = IntegerField(u'Temps de préparation')
    cookingTime = IntegerField(u'Temps de cuisson')
    categoryID = SelectField(u'Type de plat', choices = [a.values() for a in model.getCategories()],
        coerce=int, validators=[validators.Required()])

    steps = FieldList(TextField('Etape', [validators.required()]))

class RegisterForm(Form):
    login = TextField(u'Login', [validators.Required()])
    password = PasswordField('Mot de passe', [
        validators.Required(),
        validators.EqualTo('confirm', message=u'Les mots de passe doivent être identiques')
    ])
    confirm = PasswordField(u'Répétez mot de passe')

class LoginForm(Form):
    login = TextField(u'Login', [validators.Required()])
    password = PasswordField('Mot de passe', [validators.Required()])
