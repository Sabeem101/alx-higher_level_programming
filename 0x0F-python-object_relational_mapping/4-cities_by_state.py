#!/usr/bin/python3
"""
Lists all cities from the database 'hbtn_0e_4_usa'.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Connects to the database and get the cities
    from the database.
    """
    DB = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    with DB.cursor() as crsr:
        crsr.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)
    rows = crsr.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
