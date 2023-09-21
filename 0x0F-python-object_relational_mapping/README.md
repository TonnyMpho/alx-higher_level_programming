## Python - Object-relational mapping

##### Databases and Python!

We are using the module __MySQLdb__ to connect to a __MySQL__ database and execute SQL queries.
And we will use the module __SQLAlchemy__ an Object Relational Mapper (ORM).


#### Object-relational Mappers (ORMs)

An object-relational mapper (ORM) is a code library that automates the transfer of data stored in relational database tables into objects that are more commonly used in application code.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

#### Read:
- [Object-relational mappers](https://www.fullstackpython.com/object-relational-mappers-orms.html)
- [Python MySQL Documentation](https://www.mikusa.com/python-mysql-docs/index.html)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)
- [mysqlclient repo](https://github.com/PyMySQL/mysqlclient#install)
- [Python SQLAlchemy Cheatsheet](https://www.pythonsheets.com/notes/python-sqlalchemy.html)
- [SQLAlchemy ORM Tutorial for Python Developers](https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/)
- [Python Virtual Environments](https://realpython.com/python-virtual-environments-a-primer/)

#### Install and activate venv

To create a Python Virtual Environment, allowing to install specific dependencies.
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```

#### Install MySQLdb module

For installing MySQLdb, you need to have MySQL installed.
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```
#### if having errors or trouble insatlling mysqlclient try:
```
$ sudo pip install --no-binary :all: mysqlclient
$ python -c "import MySQLdb"
```
#### Install SQLAlchemy
```
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

### Tasks

- Code should not be executed when imported
- MySQL server running on localhost at port 3306

- Exception
	- (no argument validation needed)

0. Get all states 
	- ##### script that lists all states from the database
	- module MySQLdb (import MySQLdb)
	- sorted in ascending order by states.id

1. Filter states
	- ##### script that lists all states with a name starting with N (upper N) from the database

2. Filter states by user input
	- ##### script that takes in an argument and displays all values in the states table where name matches the argument

3. SQL Injection
	- ##### cript that takes in arguments and displays all values in the states table where name matches the argument. But this time, one that is safe from MySQL injections!

4. Cities by states
	- ##### script that lists all cities from the database
	- sorted in ascending order by cities.id

5. All cities by state
	- ##### script that takes in the name of a state as an argument and lists all cities of that state
