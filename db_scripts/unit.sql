DROP TABLE IF EXISTS Unit;

CREATE TABLE Unit
(
        unitID          INTEGER(2)      NOT NULL        AUTO_INCREMENT
,       unitName        VARCHAR(10)     NOT NULL

,       CONSTRAINT      pk_unit         PRIMARY KEY (unitID)
);