# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from  MySQLdb.cursors import DictCursor
from project import mysql
import sys

class Model(object):
    def __init__(self, mysql):
        self.conn = mysql.connect()
        self.cursor = self.conn.cursor(DictCursor)
        pass

    ########################### Unit ###########################

    def getUnits(self):
        self.cursor.execute("SELECT unitID, unitName FROM Unit")
        rows = self.cursor.fetchall()
        return rows

    ########################### Category ###########################

    def getCategories(self):
        self.cursor.execute("SELECT categoryID, categoryName FROM Category")
        rows = self.cursor.fetchall()
        return rows

    def getCategoryCountById(self, id):
        self.cursor.execute("SELECT count(*) AS categoryCount FROM Recipe WHERE categoryID = %s", (id,))
        row = self.cursor.fetchone()
        return row

    ########################### Recipe ###########################
    def getRecipes(self):
        sql = """
            SELECT Recipe.recipeID, recipeName, image, login, ((IFNULL(AVG(tasteScore), 0) + IFNULL(AVG(priceScore), 0) + IFNULL(AVG(instructionScore), 0)) / 3) AS avgScore
            FROM Recipe
            JOIN User ON User.userID = Recipe.userID
            LEFT OUTER JOIN Comment ON Comment.recipeID = Recipe.recipeID
            GROUP BY Recipe.recipeID
            """
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def getRecipesByUserID(self, userID):
        sql = """
              SELECT Recipe.recipeID, recipeName, image, ((IFNULL(AVG(tasteScore), 0) + IFNULL(AVG(priceScore), 0) + IFNULL(AVG(instructionScore), 0)) / 3) AS avgScore
              FROM Recipe
              LEFT OUTER JOIN Comment ON Comment.recipeID = Recipe.recipeID
              WHERE Recipe.userID = %s
              GROUP BY Recipe.recipeID
              """
        self.cursor.execute(sql, (userID,))
        rows = self.cursor.fetchall()
        return rows

    def getRecipe(self, id):
        sql = """
              SELECT recipeID, recipeName, image, budget, difficulty, categoryName,
              preparationTime, cookingTime, Recipe.userID, login
              FROM Recipe
              JOIN User on User.userID = Recipe.userID
              JOIN Category on Category.categoryID = Recipe.categoryID
              WHERE recipeID = %s
              """
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return row

    def getBestRecipeByCategoryId(self, id):
        sql = """
              SELECT Recipe.recipeID, recipeName, image, login, averageScore
              FROM Recipe
              JOIN User on User.userID = Recipe.userID
              JOIN Average ON Average.recipeID = Recipe.recipeID
              WHERE categoryID = %s
              GROUP BY averageScore
              HAVING averageScore = (SELECT MAX(averageScore) FROM Average JOIN Recipe ON Average.recipeID = Recipe.recipeID WHERE Recipe.categoryID = %s)
              """
        self.cursor.execute(sql, (id,id,))
        row = self.cursor.fetchone()
        return row

    def insertRecipe(self, recipeName, image, budget, difficulty, preparationTime, cookingTime, userID, categoryID):
        try:
            sql = """
                INSERT INTO Recipe (recipeName, image, budget, difficulty,
                preparationTime, cookingTime, userID, categoryID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            self.cursor.execute(sql, (recipeName, image, budget, difficulty, preparationTime, cookingTime, userID, categoryID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Average ###########################
    def getAverageByRecipeID(self, recipeID):
        sql = """
            SELECT averageScore, tasteAvgScore, instructionAvgScore, priceAvgScore
            FROM Average
            WHERE recipeID = %s"""
        self.cursor.execute(sql, (recipeID,))
        row = self.cursor.fetchone()
        return row

    ########################### Step ###########################
    def getStepsByRecipeID(self, recipeID):
        sql = """
            SELECT stepID, stepCount, stepDescription
            FROM Step
            WHERE recipeID = %s
            ORDER BY stepCount"""
        self.cursor.execute(sql, (recipeID,))
        rows = self.cursor.fetchall()
        return rows

    def insertStep(self, stepCount, stepDescription, recipeID):
        try:
            sql = """
                INSERT INTO Step (stepCount, stepDescription, recipeID)
                VALUES (%s, %s, %s)
                """
            self.cursor.execute(sql, (stepCount, stepDescription, recipeID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Contain ###########################
    def insertContain(self, recipeID, ingredientID, quantity, isMain, unitID):
        try:
            sql = """
                INSERT INTO Contain (recipeID, ingredientID, quantity, isMain, unitID)
                VALUES (%s, %s, %s, %s, %s)
                """
            self.cursor.execute(sql, (recipeID, ingredientID, quantity, isMain, unitID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def getContainsByRecipeID(self, recipeID):
        sql = """
            SELECT recipeID, quantity, isMain, ingredientName, unitName
            FROM Contain
            JOIN Ingredient ON Ingredient.ingredientID = Contain.ingredientID
            JOIN Unit ON Unit.unitID = Contain.unitID
            WHERE recipeID = %s
            ORDER BY recipeID"""
        self.cursor.execute(sql, (recipeID,))
        rows = self.cursor.fetchall()
        return rows
    ########################### Ingredient ###########################
    def getIngredients(self):
        sql = """
        SELECT ingredientID, ingredientName
        FROM Ingredient"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def getIngredientByName(self, ingredientName):
        sql = """
        SELECT ingredientID, ingredientName
        FROM Ingredient
        WHERE ingredientName = %s"""
        self.cursor.execute(sql, (ingredientName,))
        row = self.cursor.fetchone()
        return row

    def insertIngredient(self, ingredientName):
        try:
            sql = """INSERT INTO Ingredient (ingredientName) VALUES (%s)"""
            self.cursor.execute(sql, (ingredientName,))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Comment ###########################
    def insertComment(self, comment, tasteScore, priceScore, instructionScore, userID, recipeID):
        try:
            sql = """
            INSERT INTO Comment (comment, tasteScore, priceScore, instructionScore, userID, recipeID)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(sql, (comment, tasteScore, priceScore, instructionScore, userID, recipeID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def getCommentsByRecipeID(self, recipeID):
        sql = """
        SELECT comment, tasteScore, priceScore, instructionScore, commentDate, login
        FROM Comment
        JOIN User on User.userID = Comment.userID
        WHERE recipeID = %s
        ORDER BY commentDate DESC"""
        self.cursor.execute(sql, (recipeID,))
        rows = self.cursor.fetchall()
        return rows


    ########################### User ###########################
    def getUsers(self):
        sql = """SELECT userID, login FROM User"""
        self.cursor.execute(sql)
        rows = self.cursor.fetchall()
        return rows

    def getUserById(self, id):
        sql = """SELECT userID, login, password FROM User WHERE userID = %s"""
        self.cursor.execute(sql, (id,))
        row = self.cursor.fetchone()
        return row

    def getUserPriceAvg(self, id):
        sql = """
              SELECT AVG(budget) as priceAvg
              FROM Recipe
              WHERE userID = %s
              """
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
            self.cursor.execute(sql, (login, password))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Ranking ###########################
    def getRanking_QP(self, id):
        sql = """
              SELECT Recipe.recipeID, recipeName, image, login, ((IFNULL(AVG(tasteScore), 0) + IFNULL(AVG(priceScore), 0) + IFNULL(AVG(instructionScore), 2)) / (3 * budget)) AS QP
              FROM Recipe
              JOIN User ON User.userID = Recipe.userID
              LEFT OUTER JOIN Comment ON Comment.recipeID = Recipe.recipeID
              GROUP BY Recipe.recipeID
              ORDER BY QP DESC
              LIMIT %s
              """
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

    def getRanking_FastDesserts(self, id):
        sql = """
              SELECT recipeID, recipeName, image, login, (preparationTime + cookingTime) AS totalTime
              FROM Recipe
              JOIN User ON User.userID = Recipe.userID
              JOIN Category ON Category.categoryID = Recipe.categoryID
              WHERE Category.categoryName = 'Dessert'
              ORDER BY totalTime ASC
              LIMIT %s
              """
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

    def getRanking_MostCommented(self, id):
        sql = """
              SELECT Recipe.recipeID, recipeName, image, login, count(*) AS nbCom
              FROM Recipe
              JOIN User ON User.userID = Recipe.userID
              JOIN Comment ON Comment.recipeID = Recipe.recipeID
              GROUP BY Recipe.recipeID
              ORDER BY nbCom DESC
              LIMIT %s
              """
        self.cursor.execute(sql, (id,))
        rows = self.cursor.fetchall()
        return rows

model = Model(mysql)
