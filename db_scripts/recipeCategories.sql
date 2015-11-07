DROP TABLE IF EXISTS RecipeCategories;

CREATE TABLE RecipeCategories
(
        recipeID        INTEGER(10)     NOT NULL
,       categoryID      INTEGER(2)      NOT NULL

,       CONSTRAINT      pk_recipecat    PRIMARY KEY (recipeID, categoryID)
,       CONSTRAINT      fk_recipe       FOREIGN KEY (recipeID) REFERENCES Recipe(recipeID)
,       CONSTRAINT      fk_category     FOREIGN KEY (categoryID) REFERENCES Category(categoryID)
);