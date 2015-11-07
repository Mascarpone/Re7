DROP TABLE IF EXISTS Ingredient;

CREATE TABLE Ingredient
(
        ingredientID        INTEGER(5)      NOT NULL        AUTO_INCREMENT
,       ingredientName      VARCHAR(30)     NOT NULL
,       unitID              INTEGER(2)      NOT NULL

,       CONSTRAINT          pk_ingredient   PRIMARY KEY (ingredientID)
,       CONSTRAINT          fk_unit         FOREIGN KEY (unitID) REFERENCES Unit(unitID)
);