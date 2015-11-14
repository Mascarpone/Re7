# -*- coding: utf-8 -*-
from  MySQLdb.cursors import DictCursor
from project import mysql
import sys

class Model(object):
    def __init__(self, mysql):
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor(DictCursor)
        pass

    def getUnits(self):
        self.cursor.execute("SELECT unitID, unitName FROM Unit")
        rows = self.cursor.fetchall()
        return rows

    def getCategories(self):
        self.cursor.execute("SELECT categoryID, categoryName FROM Category")
        rows = self.cursor.fetchall()
        return rows

    ########################### Recipe ###########################
    def getRecipes(self):
        sql = """
            SELECT recipeID, recipeName
            FROM Recipe"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def getRecipe(self, id):
        sql = """
            SELECT recipeID, recipeName, budget, difficulty,
            preparationTime, cookingTime
            FROM Recipe
            WHERE recipeID = %s"""
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return row

    def insertRecipe(self, recipeName, budget, difficulty, preparationTime, cookingTime, userID, categoryID):
        try:
            sql = """
                INSERT INTO Recipe (recipeName, budget, difficulty,
                preparationTime, cookingTime, userID, categoryID)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
            res = self.cursor.execute(sql, (recipeName, budget, difficulty, preparationTime, cookingTime, userID, categoryID))
            self.conn.commit()
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### User ###########################
    def getUserById(self, id):
        sql = """SELECT userID, login, password FROM User WHERE userID = %s"""
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return row

    def getUserByLogin(self, login):
        sql = """SELECT userID, login, password FROM User WHERE login = %s"""
        self.cursor.execute(sql, (login,))
        row = self.cursor.fetchone()
        return row

    def getUserByLoginAndPassword(self, login, password):
        sql = """SELECT userID, login, password FROM User WHERE login = %s AND password = %s"""
        self.cursor.execute(sql, (login, password))
        row = self.cursor.fetchone()
        return row

    def insertUser(self, login, password):
        try:
            sql = """INSERT INTO User (login, password) VALUES (%s, %s)"""
            res = self.cursor.execute(sql, (login, password))
            self.conn.commit()
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Ingredient ###########################
    def getIngredients(self):
        sql = """
        SELECT ingredientID, ingredientName
        FROM Ingredient"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

model = Model(mysql)
