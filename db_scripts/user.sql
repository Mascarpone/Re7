DROP TABLE IF EXISTS User;

CREATE TABLE User
(
        userID          INTEGER(5)          NOT NULL        PRIMARY KEY     AUTO_INCREMENT
,       login           VARCHAR(30)         NOT NULL
,       password        VARCHAR(30)         NOT NULL

,       CONSTRAINT      chk_login           CHECK (LEN(login) >= 6)
,       CONSTRAINT      chk_password        CHECK (LEN(password) >= 8)
)