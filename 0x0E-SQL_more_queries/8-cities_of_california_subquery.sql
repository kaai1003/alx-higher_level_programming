-- list all cities of california state
-- result sorted in ascending
SELECT id, name
  FROM cities
 WHERE state_id IN
       (SELECT id
	  FROM states
	 WHERE name = "California")
 ORDER BY id;