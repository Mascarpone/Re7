# -*- coding: utf-8 -*-
from default import model
from flask.ext.wtf import Form
from wtforms import FormField, SelectField, TextField, TextAreaField, IntegerField, FieldList, PasswordField, BooleanField, validators
from flask_wtf.file import FileField, FileAllowed
from project import gallery

class ContainForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        Form.__init__(self, *args, **kwargs)

    isMain = BooleanField(u'Principal')
    quantity = IntegerField(u'Quantité')
    unitID = SelectField(u'Mesure', choices = [(a['unitID'], a['unitName']) for a in model.getUnits()],
        coerce=int, validators=[validators.Required()])
    #ingredientID = SelectField(u'Ingrédient', choices = [a.values() for a in model.getIngredients()],
    #    coerce=int, validators=[validators.Required()])
    ingredientName = TextField(u'Ingrédient', validators=[validators.Required()])

class RecipeForm(Form):
    image = FileField('Image', [validators.optional(), FileAllowed(gallery, "Images only!")])
    recipeName = TextField(u'Nom de la recette', [validators.Required()])
    budget = IntegerField(u'Budget')
    difficulty = IntegerField(u'Difficulté', [validators.Required(), validators.NumberRange(min=1, max=5)])
    preparationTime = IntegerField(u'Temps de préparation')
    cookingTime = IntegerField(u'Temps de cuisson')
    categoryID = SelectField(u'Type de plat', choices = [a.values() for a in model.getCategories()],
        coerce=int, validators=[validators.Required()])

    steps = FieldList(TextAreaField('Etape', [validators.required()]))
    contains = FieldList(FormField(ContainForm), min_entries=1)

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


class CommentForm(Form):
    comment = TextAreaField('Commentaire')
    tasteScore = IntegerField(u'Qualité gastronomique', [validators.Required(), validators.NumberRange(min=1, max=5)])
    priceScore = IntegerField(u'Respect du budget', [validators.Required(), validators.NumberRange(min=1, max=5)])
    instructionScore = IntegerField(u'Clareté des instructions', [validators.Required(), validators.NumberRange(min=1, max=5)])
