DROP TABLE IF EXISTS Recipe;

CREATE TABLE Recipe
(
        recipeID            INTEGER(10)     NOT NULL        AUTO_INCREMENT
,       recipeName          VARCHAR(50)     NOT NULL
,       budget              INTEGER(3)      NOT NULL
,       difficulty          INTEGER(1)      NOT NULL
,       preparationTime     INTEGER(4)      NOT NULL
,       cookingTime         INTEGER(4)
,       userID              INTEGER(5)      NOT NULL

,       CONSTRAINT          pk_recipe       PRIMARY KEY (recipeID)
,       CONSTRAINT          fk_author       FOREIGN KEY (userID) REFERENCES User(userID)
,       CONSTRAINT          chk_difficulty  CHECK (difficulty >= 0 AND difficulty <= 5)
);