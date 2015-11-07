DROP TABLE IF EXISTS RecipeIngredients;

CREATE TABLE RecipeIngredients
(
        recipeID        INTEGER(10)         NOT NULL
,       ingredientID    INTEGER(5)          NOT NULL
,       quantity        FLOAT(6, 2)         NOT NULL
,       isMain          BOOLEAN             NOT NULL        DEFAULT 0

,       CONSTRAINT      pk_recipeing        PRIMARY KEY (recipeID, ingredientID)
,       CONSTRAINT      fk_recipe           FOREIGN KEY (recipeID) REFERENCES Recipe(recipeID)
,       CONSTRAINT      fk_ingredient       FOREIGN KEY (ingredientID) REFERENCES Ingredient(ingredientID)
);