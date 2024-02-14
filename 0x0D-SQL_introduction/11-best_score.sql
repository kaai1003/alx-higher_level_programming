-- list records with score >= 10 in second table 
-- hould display both the score and the name
-- Records will be ordered by score (top first)
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
