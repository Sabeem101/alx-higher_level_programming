-- A script that lists all of the cities of California,
-- that can be found in the database 'hbtn_0d_usa' in the MYSQL server.
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California") ORDER BY cities.id ASC;
