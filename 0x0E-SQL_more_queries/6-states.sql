-- create "hbtn_0d_usa" database
-- create "state" table in "hbtn_0d_usa" db
-- id: auto generated unique primary key and not NULL
-- name: varchar(256) not NULL
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    PRIMARY KEY(id),
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);