#!/usr/bin/python3

"""
This script lists all states with a name matching the argument,
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    hs = 'localhost'
    DB = MySQLdb.connect(host=hs, user=a[1], passwd=a[2], db=a[3], port=3306)
    C = DB.cursor()
    q = "SELECT * FROM states WHERE BINARY name='{}' ORDER BY id".format(a[4])
    C.execute(q)
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
