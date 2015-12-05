# -*- coding: utf-8 -*-
from default import model
from flask.ext.wtf import Form
from wtforms import widgets, FormField, SelectField, SelectMultipleField, TextField, RadioField, TextAreaField, IntegerField, FloatField, FieldList, PasswordField, BooleanField, validators
from flask_wtf.file import FileField, FileAllowed
from project import gallery

class SearchForm(Form):
    categories = SelectMultipleField(
        u'Catégories',
        choices=[(a['categoryID'], a['categoryName']) for a in model.getCategories()],
        coerce=int,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )
    ingredients = SelectMultipleField(
        u'Ingrédients',
        choices=[(a['ingredientID'], a['ingredientName']) for a in model.getIngredients()],
        coerce=int,
        option_widget=widgets.CheckboxInput(),
        widget=widgets.ListWidget(prefix_label=False)
    )
    max = model.getMaxBudget()
    min = model.getMinBudget()
    minprice = IntegerField(u'Min', default=int(min['MIN(budget)']))
    maxprice = IntegerField(u'Max', default=int(max['MAX(budget)']))
    query = TextField(u'Recherche')

class ContainForm(Form):
    def __init__(self, *args, **kwargs):
        kwargs['csrf_enabled'] = False
        Form.__init__(self, *args, **kwargs)

    isMain = BooleanField(u'Principal')
    quantity = IntegerField(u'Quantité')
    unitID = SelectField(u'Mesure', choices = [(a['unitID'], a['unitName']) for a in model.getUnits()],
        coerce=int, validators=[validators.Required()])
    ingredientName = TextField(u'Ingrédient', validators=[validators.Required()])

class RecipeForm(Form):
    image = FileField('Image', [validators.optional(), FileAllowed(gallery, "Images only!")])
    recipeName = TextField(u'Nom de la recette', [validators.Required()])
    budget = FloatField(u'Budget')
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
    tasteScore = RadioField(u'Qualité gastronomique', choices=[(i+1, i+1) for i in range(5)], coerce=int, validators=[validators.Required()])
    priceScore = RadioField(u'Respect du budget', choices=[(i+1, i+1) for i in range(5)], coerce=int, validators=[validators.Required()])
    instructionScore = RadioField(u'Clareté des instructions', choices=[(i+1, i+1) for i in range(5)], coerce=int, validators=[validators.Required()])
