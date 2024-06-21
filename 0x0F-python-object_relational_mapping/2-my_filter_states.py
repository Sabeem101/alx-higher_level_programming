#!/usr/bin/python3
"""
Takes in an argument and displays all values
in the states table of 'hbtn_0e_0_usa' where
the name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Connects to the database and fetches
    all data from the 'states' table.
    """
    DB = MySQLdb.connect(
            host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3])

    crsr = DB.cursor()
    crsr.execute(
            "SELECT * FROM states \
            WHERE name LIKE BINARY '{}' \
            ORDER BY states.id ASC".format(argv[4]))
    rows = crsr.fetchall()

    for row in rows:
        print(row)
