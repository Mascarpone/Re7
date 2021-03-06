# -*- coding: utf-8 -*-
from  MySQLdb.cursors import DictCursor
from project import mysql
import sys

class Model(object):
    def __init__(self, mysql):
        self.conn = mysql.connect()
        self.conn.ping(True)
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
    def getRecipesSearch(self, minprice, maxprice, ingredients, categories, query):
        cat = ""
        if categories:
            cat = "AND categoryID in ({0})".format( ', '.join([str(i) for i in categories]))

        ingr = ""
        if ingredients:
            ingr = "AND ingredientID in ({0})".format( ', '.join([str(i) for i in ingredients]))


        sql = """
            SELECT DISTINCT Recipe.recipeID, recipeName, image, login, ((IFNULL(AVG(tasteScore), 0) + IFNULL(AVG(priceScore), 0) + IFNULL(AVG(instructionScore), 0)) / 3) AS avgScore
            FROM Recipe
            JOIN User ON User.userID = Recipe.userID
            JOIN Contain ON Contain.recipeID = Recipe.recipeID
            LEFT OUTER JOIN Comment ON Comment.recipeID = Recipe.recipeID
            WHERE (recipeName like %s OR login like %s) AND budget BETWEEN %s AND %s {0} {1}
            GROUP BY Recipe.recipeID
            """.format(cat, ingr)
        #assert False
        self.cursor.execute(sql, ("%"+query+"%", "%"+query+"%", minprice, maxprice))
        rows = self.cursor.fetchall()
        return rows

    def getRecipes(self):
        sql = """
            SELECT Recipe.recipeID, recipeName, image, login
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
              SELECT Recipe.recipeID, recipeName, image
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
              preparationTime, cookingTime, Recipe.userID, login, Recipe.categoryID
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
              GROUP BY averageScore, Recipe.recipeID
              HAVING averageScore = (SELECT MAX(averageScore) FROM Average JOIN Recipe ON Average.recipeID = Recipe.recipeID WHERE Recipe.categoryID = %s)
              """
        self.cursor.execute(sql, (id,id,))
        row = self.cursor.fetchone()
        return row

    def insertRecipe(self, recipeName, image, budget, difficulty, preparationTime, cookingTime, userID, categoryID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                INSERT INTO Recipe (recipeName, image, budget, difficulty,
                preparationTime, cookingTime, userID, categoryID)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                """
            self.cursor.execute(sql, (recipeName, image, budget, difficulty, preparationTime, cookingTime, userID, categoryID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def updateRecipe(self, id, recipeName, budget, difficulty, preparationTime, cookingTime, categoryID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                UPDATE Recipe
                SET recipeName = %s,
                    budget = %s,
                    difficulty = %s,
                    preparationTime = %s,
                    cookingTime = %s,
                    categoryID = %s
                WHERE recipeID = %s
                """
            self.cursor.execute(sql, (recipeName, budget, difficulty, preparationTime, cookingTime, categoryID, id))
            self.conn.commit()
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            print sql %(recipeName, budget, difficulty, preparationTime, cookingTime, categoryID, id)
            self.conn.rollback()


    def deleteRecipe(self, id):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql1 = """
                DELETE FROM Comment
                WHERE recipeID = %s
                """
            sql2 = """
                DELETE FROM Step
                WHERE recipeID = %s
                """
            sql3 = """
                DELETE FROM Contain
                WHERE recipeID = %s
                """
            sql4 = """
                DELETE FROM Recipe
                WHERE recipeID = %s
                """
            self.cursor.execute(sql1, (id,))
            self.cursor.execute(sql2, (id,))
            self.cursor.execute(sql3, (id,))
            self.cursor.execute(sql4, (id,))
            self.conn.commit()
            return True
        except:
            print self.conn.error()
            print("Error in {0}".format(sql1 + sql2 + sql3 + sql4))
            self.conn.rollback()
            return False

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
            SELECT stepCount, stepDescription
            FROM Step
            WHERE recipeID = %s
            ORDER BY stepCount"""
        self.cursor.execute(sql, (recipeID,))
        rows = self.cursor.fetchall()
        return rows

    def insertStep(self, stepCount, stepDescription, recipeID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                INSERT INTO Step (stepCount, stepDescription, recipeID)
                VALUES (%s, %s, %s)
                """
            self.cursor.execute(sql, (stepCount, stepDescription, recipeID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def updateStep(self, stepCount, stepDescription, recipeID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                UPDATE Step
                SET stepDescription = %s
                WHERE stepCount = %s AND recipeID = %s
                """
            self.cursor.execute(sql, (stepDescription, stepCount, recipeID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Contain ###########################
    def insertContain(self, recipeID, ingredientID, quantity, isMain, unitID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                INSERT INTO Contain (recipeID, ingredientID, quantity, isMain, unitID)
                VALUES (%s, %s, %s, %s, %s)
                """
            self.cursor.execute(sql, (recipeID, ingredientID, quantity, isMain, unitID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def updateContain(self, recipeID, ingredientID, quantity, isMain, unitID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
                UPDATE Contain
                SET quantity = %s,
                    isMain = %s
                WHERE recipeID = %s AND ingredientID = %s AND unitID = %s
                """
            self.cursor.execute(sql, (quantity, isMain, recipeID, ingredientID, unitID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def getContainsByRecipeID(self, recipeID):
        sql = """
            SELECT recipeID, quantity, isMain, ingredientName, unitName, Contain.unitID
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
            self.cursor = self.conn.cursor(DictCursor)
            sql = """INSERT INTO Ingredient (ingredientName) VALUES (%s)"""
            self.cursor.execute(sql, (ingredientName,))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Comment ###########################
    def insertComment(self, comment, tasteScore, priceScore, instructionScore, userID, recipeID):
        try:
            self.cursor = self.conn.cursor(DictCursor)
            sql = """
            INSERT INTO Comment (comment, tasteScore, priceScore, instructionScore, userID, recipeID)
            VALUES (%s, %s, %s, %s, %s, %s)"""
            self.cursor.execute(sql, (comment, tasteScore, priceScore, instructionScore, userID, recipeID))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    def getCommentsByRecipeID(self, recipeID):
        sql = """
        SELECT comment, tasteScore, priceScore, instructionScore, commentDate, login, Comment.userID
        FROM Comment
        JOIN User on User.userID = Comment.userID
        WHERE recipeID = %s
        ORDER BY commentDate DESC"""
        self.cursor.execute(sql, (recipeID,))
        rows = self.cursor.fetchall()
        return rows

    def getCommentsByRecipeIDAndUserID(self, recipeID, userID):
        sql = """
        SELECT comment, tasteScore, priceScore, instructionScore, commentDate, login
        FROM Comment
        JOIN User ON User.userID = Comment.userID
        WHERE recipeID = %s and User.userID = %s
        ORDER BY commentDate DESC"""
        self.cursor.execute(sql, (recipeID, userID))
        row = self.cursor.fetchone()
        return row


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
              SELECT IFNULL(AVG(budget), 0) as priceAvg
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
            self.cursor = self.conn.cursor(DictCursor)
            sql = """INSERT INTO User (login, password) VALUES (%s, %s)"""
            self.cursor.execute(sql, (login, password))
            self.conn.commit()
            return self.cursor.lastrowid
        except:
            print self.conn.error()
            print("Error in {0}".format(sql))
            self.conn.rollback()

    ########################### Ranking ###########################
    def getMaxBudget(self):
        sql = "SELECT MAX(budget) FROM Recipe"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row

    def getMinBudget(self):
        sql = "SELECT MIN(budget) FROM Recipe"
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row

    def getRanking_QP(self, id):
        sql = """
              SELECT Recipe.recipeID, recipeName, image, login, averageScore / budget AS QP
              FROM Recipe
              JOIN User ON User.userID = Recipe.userID
              JOIN Average ON Recipe.recipeID = Average.recipeID
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

    def getBestCommentator(self):
        sql = """
              SELECT User.userID, login, SQRT(sum(pow(ecart, 2))/count(*)) AS ecarttype
              FROM User
              JOIN
               (SELECT userID, ABS((tasteScore + instructionScore + priceScore)/3 - averageScore) AS ecart
                FROM Comment
                JOIN Average ON Comment.recipeID = Average.recipeID) AS Ecarts
              ON Ecarts.userID = User.userID
              GROUP BY User.userID
              HAVING ecarttype = (SELECT MIN(ecarttype)
                                  FROM
                                  (SELECT User.userID, login, SQRT(sum(pow(ecart, 2))/count(*)) AS ecarttype
                                  FROM User
                                  JOIN
                                   (SELECT userID, ABS((tasteScore + instructionScore + priceScore)/3 - averageScore) AS ecart
                                    FROM Comment
                                    JOIN Average ON Comment.recipeID = Average.recipeID) AS Ecarts
                                  ON Ecarts.userID = User.userID
                                  GROUP BY User.userID) AS MinEcarttype
                                  )
              """
        self.cursor.execute(sql)
        row = self.cursor.fetchone()
        return row

model = Model(mysql)
