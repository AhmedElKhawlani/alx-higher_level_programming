#!/usr/bin/python3

"""
This script lists all states with a name starting with N,
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    arg = sys.argv
    DB = MySQLdb.connect(host='localhost', user=arg[1], passwd=arg[2],
                     db=arg[3], port=3306)
    C = DB.cursor()
    C.execute("SELECT * FROM states ORDER BY id WHERE name LIKE 'N%'")
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
