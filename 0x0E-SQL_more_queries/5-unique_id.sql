-- create "unique_id" table
-- id: INT default 1 unique / name: VARCHAR(256) not NULL
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);