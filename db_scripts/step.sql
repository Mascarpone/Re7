DROP TABLE IF EXISTS Step;

CREATE TABLE Step
(
        recipeID        INTEGER(10)         NOT NULL
,       stepCount       INTEGER(2)          NOT NULL        -- there must not be any gap in stepCounts for a recipeID
,       stepDescription VARCHAR(256)        NOT NULL

,       CONSTRAINT      pk_step             PRIMARY KEY (recipeID, stepCount)
,       CONSTRAINT      fk_recipe           FOREIGN KEY (recipeID) REFERENCES Recipe(recipeID)
);