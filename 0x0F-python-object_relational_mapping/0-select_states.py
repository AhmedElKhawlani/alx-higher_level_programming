#!/usr/bin/python3

"""
This script lists all states from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    hs = 'localhost'
    DB = MySQLdb.connect(host=hs, user=a[1], passwd=a[2], db=a[3], port=3306)
    C = DB.cursor()
    C.execute("SELECT * FROM states ORDER BY id")
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
