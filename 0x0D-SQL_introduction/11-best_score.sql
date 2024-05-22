-- A script that lists all records with 'score>=10' in second_table,
-- of the database htbn_0c_0 in MYSQL server.
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
