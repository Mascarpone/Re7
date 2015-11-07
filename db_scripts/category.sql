DROP TABLE IF EXISTS Category;

CREATE TABLE Category
(
        categoryID      INTEGER(2)      NOT NULL        AUTO_INCREMENT
,       categoryName    VARCHAR(20)     NOT NULL

,       CONSTRAINT      pk_category     PRIMARY KEY (categoryID)
);