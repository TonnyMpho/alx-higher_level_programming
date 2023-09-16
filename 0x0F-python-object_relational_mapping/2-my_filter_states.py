#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


def select_state(username, password, dbname, name):
    """ function to connect and select from the database"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=dbname)

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name LIKE '%{}%' ORDER BY id ASC"
            .format(name))

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    select_state(username, password, dbname, name)
