#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state
"""
import MySQLdb
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=dbname, port=3306)

    cur = db.cursor()
    cur.execute("""
    SELECT cities.name FROM cities
    JOIN states ON states.id = cities.state_id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """, (state_name,))

    rows = cur.fetchall()

    print(", ".join(row[0] for row in rows))

    cur.close
    db.close
