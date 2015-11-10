# -*- coding: utf-8 -*-
from project import mysql
import sys

class Model(object):
    def __init__(self, mysql):
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor()
        pass

    def getRecipes(self):
        self.cursor.execute("SELECT recipeID, recipeName FROM Recipe")
        rows = self.cursor.fetchall()
        return rows

    def getRecipe(self, id):
        self.cursor.execute("SELECT recipeID, recipeName FROM Recipe WHERE recipeID = %s", (id))
        row = self.cursor.fetchone()
        return row

    def insertRecipe(self, recipeName, budget, difficulty, preparationTime, cookingTime, userID, categoryID):
        try:
            sql = """
            insert into re7.Recipe (recipeName, budget, difficulty, preparationTime, cookingTime, userID, categoryID)
            values (%s, %s, %s, %s, %s, %s, %s)
            """
            res = self.cursor.execute(sql, (recipeName, budget, difficulty, preparationTime, cookingTime, userID, categoryID))
            self.conn.commit()
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def getUnits(self):
        self.cursor.execute("SELECT unitID, unitName FROM Unit")
        rows = self.cursor.fetchall()
        return rows

    def getCategories(self):
        self.cursor.execute("SELECT categoryID, categoryName FROM Category")
        rows = self.cursor.fetchall()
        return rows

model = Model(mysql)
