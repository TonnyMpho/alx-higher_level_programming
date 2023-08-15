-- script that creates a table called first_table in the
-- current database in a MySQL server
-- first_table description: id INT (NUMNER), name VARCHAR(256) CHAR
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS first_table
	(id INT, name VARCHAR(256));
