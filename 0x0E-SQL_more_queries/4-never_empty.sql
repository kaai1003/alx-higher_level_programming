-- create "id_not_null" table
-- id: INT default 1 / name: VARCHAR(256) not NULL
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);