#!/usr/bin/python3
"""
Lists all states from the database 'hbtn_0e_0_usa'.
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """
    Connects to the database & fetches all data
    from the 'states' table.
    """
    DB = MySQLdb.connect(
            host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    crsr = DB.cursor()
    crsr.execute("SELECT * FROM states")
    rows = crsr.fetchall()

    for row in rows:
        print(row)
