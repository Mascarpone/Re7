-- -----------------------------------------------------
-- Schema re7
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS re7;

CREATE SCHEMA IF NOT EXISTS re7;
USE re7 ;


-- -----------------------------------------------------
-- Clean base
-- -----------------------------------------------------
DROP TABLE IF EXISTS re7.Step ;
DROP VIEW IF EXISTS Average;
DROP TABLE IF EXISTS re7.Comment ;
DROP TABLE IF EXISTS re7.Contain ;
DROP TABLE IF EXISTS re7.Ingredient ;
DROP TABLE IF EXISTS re7.Unit ;
DROP TABLE IF EXISTS re7.Recipe ;
DROP TABLE IF EXISTS re7.Category ;
DROP TABLE IF EXISTS re7.User ;


-- -----------------------------------------------------
-- Table re7.User
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.User (
    userID        INT           NOT NULL    AUTO_INCREMENT
,   login         VARCHAR(45)   NOT NULL
,   password      VARCHAR(45)   NOT NULL

,   CONSTRAINT    pk_user       PRIMARY KEY (userID)
);


-- -----------------------------------------------------
-- Table re7.Category
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Category (
    categoryID    INT           NOT NULL    AUTO_INCREMENT
,   categoryName  VARCHAR(45)   NOT NULL

,   CONSTRAINT    pk_category   PRIMARY KEY (categoryID)
);


-- -----------------------------------------------------
-- Table re7.Recipe
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Recipe (
    recipeID          INT         NOT NULL  AUTO_INCREMENT
,   recipeName        VARCHAR(45) NOT NULL
,   image             VARCHAR(60) NOT NULL
,   budget            FLOAT(5, 2) NOT NULL
,   difficulty        INT(1)      NOT NULL
,   preparationTime   INT         NOT NULL
,   cookingTime       INT         NOT NULL
,   userID            INT         NOT NULL
,   categoryID        INT         NOT NULL

,   CONSTRAINT        pk_recipe               PRIMARY KEY (recipeID)
,   CONSTRAINT        fk_recipe_user          FOREIGN KEY (userID)      REFERENCES re7.User (userID)
,   CONSTRAINT        fk_recipe_category      FOREIGN KEY (categoryID)  REFERENCES re7.Category (categoryID)
,   CONSTRAINT        chk_difficulty          CHECK (difficulty >= 1 AND difficulty <= 5)
);


-- -----------------------------------------------------
-- Table re7.Unit
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Unit (
    unitID      INT           NOT NULL    AUTO_INCREMENT
,   unitName    VARCHAR(45)   NOT NULL

,   CONSTRAINT  pk_unit       PRIMARY KEY (unitID)
);


-- -----------------------------------------------------
-- Table re7.Ingredient
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Ingredient (
    ingredientID    INT             NOT NULL    AUTO_INCREMENT
,   ingredientName  VARCHAR(45)     NOT NULL

,   CONSTRAINT      pk_ingredient   PRIMARY KEY (ingredientID)
);


-- -----------------------------------------------------
-- Table re7.Contain
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Contain (
    recipeID        INT         NOT NULL
,   ingredientID    INT         NOT NULL
,   quantity        FLOAT(5, 2) NOT NULL
,   isMain          TINYINT(1)  NOT NULL      DEFAULT 0
,   unitID          INT         NOT NULL

,   CONSTRAINT      pk_contain                PRIMARY KEY (recipeID, ingredientID, unitID)
,   CONSTRAINT      fk_contain_recipe         FOREIGN KEY (recipeID) REFERENCES re7.Recipe (recipeID)
,   CONSTRAINT      fk_contain_ingredient     FOREIGN KEY (ingredientID) REFERENCES re7.Ingredient (ingredientID)
,   CONSTRAINT      fk_contain_unit           FOREIGN KEY (unitID) REFERENCES re7.Unit (unitID)
);


-- -----------------------------------------------------
-- Table re7.Comment
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Comment (
    commentID         INT           NOT NULL  AUTO_INCREMENT
,   comment           VARCHAR(300)
,   tasteScore        INT(1)        NOT NULL
,   priceScore        INT(1)        NOT NULL
,   instructionScore  INT(1)        NOT NULL
,   commentDate       TIMESTAMP     NOT NULL  DEFAULT CURRENT_TIMESTAMP
,   userID            INT           NOT NULL
,   recipeID          INT           NOT NULL

,   CONSTRAINT      pk_comment              PRIMARY KEY (commentID)
,   CONSTRAINT      fk_comment_user         FOREIGN KEY (userID) REFERENCES re7.User(userID)
,   CONSTRAINT      fk_comment_recipe       FOREIGN KEY (recipeID) REFERENCES re7.Recipe(recipeID)
,   CONSTRAINT      chk_tasteScore          CHECK (tasteScore >= 1 AND tasteScore <= 5)
,   CONSTRAINT      chk_priceScore          CHECK (priceScore >= 1 AND priceScore <= 5)
,   CONSTRAINT      chk_instructionScore    CHECK (instructionScore >= 1 AND instructionScore <= 5)
);


-- -----------------------------------------------------
-- View re7.Average
-- -----------------------------------------------------
CREATE VIEW Average AS
SELECT recipeID, (AVG(tasteScore)+AVG(priceScore)+AVG(instructionScore))/3 AS averageScore, AVG(tasteScore) AS tasteAvgScore, AVG(priceScore) AS priceAvgScore, AVG(instructionScore) AS instructionAvgScore
FROM Comment
GROUP BY recipeID;


-- -----------------------------------------------------
-- Table re7.Step
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS re7.Step (
    stepCount       INT             NOT NULL
,   stepDescription VARCHAR(300)    NOT NULL
,   recipeID        INT             NOT NULL

,   CONSTRAINT      pk_step         PRIMARY KEY (recipeID, stepCount)
,   CONSTRAINT      fk_step_recipe  FOREIGN KEY (recipeID) REFERENCES re7.Recipe(recipeID)
);
