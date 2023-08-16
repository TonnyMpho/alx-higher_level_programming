-- script that lists all cities contained in the database hbtn_0d_usa.
-- Each record should display: cities.id - cities.name - states.name
-- Results sorted in ascending order by cities.id

SELECT cities.id, cities.name, state.name
FROM cities JOIN states ON cities.state_id = state.id
ORDER BY cities.id ASC;