-- create db "hbtn_0d_usa" and table "cities"
-- id / state_id / name
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    PRIMARY KEY(id),
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    FOREIGN KEY(state_id) REFERENCES state(id),
    name VARCHAR(256) NOT NULL
);