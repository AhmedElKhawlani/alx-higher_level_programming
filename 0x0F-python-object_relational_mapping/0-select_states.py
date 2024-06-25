#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import os

if __name__ == '__main__':
    arg = os.argv
    DB = MySQLdb.connect(host='localhost', user=arg[1], passwd=arg[2],
                     db=arg[3], port=3306)
    C = DB.cursor()
    C.execute("SELECT * FROM states")
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
