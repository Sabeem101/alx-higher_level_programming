#!/usr/bin/python3
"""
Takes in arguments and displays all values
in the states table of 'hbtn_0e_0_usa' where
name matches the argument.
But this time,
this one is safe from MYSQL injections!
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Connects to the database and fetches
    all data from the 'states' table.
    """
    DB = MySQLdb.connect(
                host="localhost", user=argv[1], port=3306,
                passwd=argv[2], db=argv[3])

    crsr = DB.cursor()
    crsr.execute("""
        SELECT
            *
        FROM
            states
        WHERE
            name LIKE BINARY %(name)s
        ORDER BY
            states.id ASC
        """, {
            'name': argv[4]
        })

    rows = crsr.fetchall()
    if rows is not None:
        for row in rows:
            print(row)
