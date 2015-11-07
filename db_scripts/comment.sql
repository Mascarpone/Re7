DROP TABLE IF EXISTS Comment;

CREATE TABLE Comment
(
        commentID           INTEGER(10)         NOT NULL        AUTO_INCREMENT
,       comment             VARCHAR(256)
,       tasteScore          INTEGER(1)          NOT NULL
,       priceScore          INTEGER(1)          NOT NULL
,       instructionScore    INTEGER(1)          NOT NULL
,       commentDate         TIMESTAMP           NOT NULL        DEFAULT CURRENT_TIMESTAMP
,       userID              INTEGER(5)          NOT NULL
,       recipeID            INTEGER(10)         NOT NULL

,       CONSTRAINT      pk_comment              PRIMARY KEY (commentID)
,       CONSTRAINT      fk_user                 FOREIGN KEY (userID) REFERENCES User(userID)
,       CONSTRAINT      fk_recipe               FOREIGN KEY (recipeID) REFERENCES Recipe(recipeID)
,       CONSTRAINT      chk_tasteScore          CHECK (tasteScore >= 0 AND tasteScore <= 5)
,       CONSTRAINT      chk_priceScore          CHECK (priceScore >= 0 AND priceScore <= 5)
,       CONSTRAINT      chk_instructionScore    CHECK (instructionScore >= 0 AND instructionScore <= 5)
);