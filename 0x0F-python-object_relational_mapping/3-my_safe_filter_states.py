#!/usr/bin/python3

"""
This script lists all states with a name matching the argument,
from the database hbtn_0e_0_usa.
Safe from SQL Injection.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    hs = 'localhost'
    DB = MySQLdb.connect(host=hs, user=a[1], passwd=a[2], db=a[3], port=3306)
    C = DB.cursor()
    s = a[4]
    C.execute("SELECT * FROM states WHERE BINARY name = %s ORDER BY id", (s,))
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
