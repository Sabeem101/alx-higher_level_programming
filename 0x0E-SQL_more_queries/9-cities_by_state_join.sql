-- A script that lists all the cities contained in the database 'hbtn_0d_usa'.
SELECT cities.id, cities.name, states.name
FROM cities LEFT JOIN states on states.id = cities.state_id
ORDER BY cities.id;
