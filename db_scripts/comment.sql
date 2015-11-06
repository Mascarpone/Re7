DROP TABLE IF EXISTS Comment;

CREATE TABLE Comment
(
        commentID           INTEGER(10)         NOT NULL        PRIMARY KEY         AUTO_INCREMENT
,       comment             VARCHAR(1024)
,       tasteScore          INTEGER(1)          NOT NULL
,       priceScore          INTEGER(1)          NOT NULL
,       instructionScore    INTEGER(1)          NOT NULL

,       CONSTRAINT      chk_tasteScore          CHECK (tasteScore >= 0 AND tasteScore <= 5)
,       CONSTRAINT      chk_priceScore          CHECK (priceScore >= 0 AND priceScore <= 5)
,       CONSTRAINT      chk_instructionScore    CHECK (instructionScore >= 0 AND instructionScore <= 5)
)