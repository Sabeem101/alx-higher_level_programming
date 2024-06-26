#!/usr/bin/python3
"""
Takes in the name of a state as an argument
and lists all cities of that state
using the database 'hbtn_0e_4_usa'.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Connects to the database and gets the cities
    from the database table.
    """
    DB = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    crsr = DB.cursor()
    crsr.execute("""
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %(state_name)s
        ORDER BY
            cities.id ASC
    """, {
        'state_name': argv[4]
    })

    rows = crsr.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
