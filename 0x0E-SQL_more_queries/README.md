## 0x0E. SQL - More queries

__SQL__
__MySQL__

### Resources
##### Read or watch:

- [How To Create a New User and Grant Permissions in MySQL](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)
- [How To Use MySQL GRANT Statement To Grant Privileges To a User](https://www.mysqltutorial.org/mysql-grant.aspx)
- [MySQL constraints](https://zetcode.com/mysql/constraints/)
- [SQL technique: subqueries](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/subqueries.php)
- [Basic query operation: the join](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/join.php)
- [SQL technique: multiple joins and the distinct keyword](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/multijoin.php)
- [SQL technique: join types](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/jointypes.php)
- [SQL technique: union and minus](https://web.csulb.edu/colleges/coe/cecs/dbdesign/dbdesign.php?page=sql/setops.php)
- [MySQL Cheat Sheet](https://intellipaat.com/mediaFiles/2019/02/SQL-Commands-Cheat-Sheet.pdf?US)
- [The Seven Types of SQL Joins](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)
- [MySQL Tutorial](https://www.youtube.com/watch?v=yPu6qV5byu4)
- [SQL Style Guide](https://www.sqlstyle.guide/)
- [MySQL 8.0 SQL Statement Syntax](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)

##### Extra resources around relational database model design:

- [Design](https://www.guru99.com/database-design.html)
- [Normalization](https://www.guru99.com/database-normalization.html)
- [ER Modeling](https://www.guru99.com/er-modeling.html)

#### How to import a SQL dump
```
$ echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
Enter password: 
$ curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
$ echo "SELECT * FROM tv_genres" | mysql -uroot -p hbtn_0d_tvshows
Enter password: 
id  name
1   Drama
2   Mystery
3   Adventure
4   Fantasy
5   Comedy
6   Crime
7   Suspense
8   Thriller
$
```

![SQL JOINS cheatsheet](https://www.bing.com/images/blob?bcid=qFKYg-XqUvYFxA)

### Tasks

### 0. My privileges!

#### A script that lists all privileges of the MySQL users **user_0d_1** and **user_0d_2** on your server (in localhost).

### 1. Root user

#### A script that creates the MySQL server user **user_0d_1**.

* __user_0d_1__ should have all privileges on your MySQL server
* The **user_0d_1** password should be set to **user_0d_1_pwd**
* If the user **user_0d_1** already exists, the script should not fail

### 2. Read user

#### A script that creates the database **hbtn_0d_2** and the user **user_0d_2**.

* **user_0d_2** should have only SELECT privilege in the database **hbtn_0d_2**
* The **user_0d_2** password should be set to **user_0d_2_pwd**
* If the database **hbtn_0d_2** already exists, script should not fail
* If the user **user_0d_2** already exists, script should not fail

### 3. Always a name

#### A script that creates the table force_name on your MySQL server.

- __force_name__ description:
	- id INT
	- name VARCHAR(256) can’t be null
- The database name will be passed as an argument of the mysql command
- If the table __force_name__ already exists, script should not fail

### 4. ID can't be null

#### A script that creates the table __id_not_null__ on your MySQL server.

- __id_not_null__ description:
	- id INT with the default value 1
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table id_not_null already exists, script should not fail

### 5. Unique ID

#### A script that creates the table __unique_id__ on your MySQL server.

- __unique_id__ description:
	- id INT with the default value 1 and must be unique
	- name VARCHAR(256)
- The database name will be passed as an argument of the mysql command
- If the table __unique_id__ already exists, script should not fail

### 6. States table

#### A script that creates the database __hbtn_0d_usa__ and the table states (in the database __hbtn_0d_usa__).

- states description:
	- id INT unique, auto generated, can’t be null and is a primary key
	- name VARCHAR(256) can’t be null
- If the database __hbtn_0d_usa__ already exists, your script should not fail
- If the table states already exists, your script should not fail

### 7. Cities table

#### A script that creates the database __hbtn_0d_usa__ and the table cities (in the database __hbtn_0d_usa__).

- cities description:
	- id INT unique, auto generated, can’t be null and is a primary key
	- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table
	- name VARCHAR(256) can’t be null
- If the database __hbtn_0d_usa__ already exists, script should not fail
- If the table cities already exists, script should not fail

### 8. Cities of California

#### A script that lists all the cities of California that can be found in the database __hbtn_0d_usa__.

- The states table contains only one record where name = California 
- Results must be sorted in ascending order by cities.id
- not allowed to use the JOIN keyword
- The database name will be passed as an argument of the mysql command

### 9. Cities by States

#### A script that lists all cities contained in the database __hbtn_0d_usa__.

- Each record should display: cities.id - cities.name - states.name
- Results must be sorted in ascending order by cities.id
- can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 10. Genre ID by show

##### Import the database dump from __hbtn_0d_tvshows__ to your MySQL server: [download](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql)

#### A script that lists all shows contained in __hbtn_0d_tvshows__ that have at least one genre linked.

- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 11. Genre ID for all shows

#### A script that lists all shows contained in the database __hbtn_0d_tvshows__.

- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- If a show doesn’t have a genre, display NULL
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 12. No genre

#### A script that lists all shows contained in __hbtn_0d_tvshows__ without a genre linked.

- Each record should display: tv_shows.title - tv_show_genres.genre_id
- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 13. Number of shows by genre

#### A script that lists all genres from __hbtn_0d_tvshows__ and displays the number of shows linked to each.

- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
- First column must be called genre
- Second column must be called number_of_shows
- Don’t display a genre that doesn’t have any shows linked
- Results must be sorted in descending order by the number of shows linked
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 14. My genres

#### A script that uses the __hbtn_0d_tvshows__ database to lists all genres of the show Dexter.

- The tv_shows table contains only one record where title = Dexter (but the id can be different)
- Each record should display: tv_genres.name
- Results must be sorted in ascending order by the genre name
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 15. Only Comedy

#### A script that lists all Comedy shows in the database __hbtn_0d_tvshows__.

- The tv_genres table contains only one record where name = Comedy (but the id can be different)
- Each record should display: tv_shows.title
- Results must be sorted in ascending order by the show title
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command

### 16. List shows and genres

#### A script that lists all shows, and all genres linked to that show, from the database __hbtn_0d_tvshows__.

- If a show doesn’t have a genre, display NULL in the genre column
- Each record should display: tv_shows.title - tv_genres.name
- Results must be sorted in ascending order by the show title and genre name
- You can use only one SELECT statement
- The database name will be passed as an argument of the mysql command
