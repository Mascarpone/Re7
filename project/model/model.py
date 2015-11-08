# -*- coding: utf-8 -*-
from project import mysql

class Model(object):
    def __init__(self, mysql):
        #self.connection = mysql.connect()
        #self.cursor = self.connection.cursor()
        pass

    def getRecipes(self):
        self.cursor.execute("SELECT recipeID, recipeName FROM Recipe")
        rows = cursor.fetchall()
        return rows

    def getRecipe(self, id):
        self.cursor.execute("SELECT recipeID, recipeName FROM Recipe WHERE recipeID = %s", (id))
        row = cursor.fetchone()
        return row

model = Model(mysql)
