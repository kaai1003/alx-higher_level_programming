-- list all records of second_table
-- rows without name will not be listed
-- score and name will displayed in descending order
SELECT score, name FROM second_table WHERE name!='' OR name IS NOT NULL ORDER BY score DESC;