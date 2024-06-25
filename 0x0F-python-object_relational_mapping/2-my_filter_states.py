#!/usr/bin/python3

"""
This script lists all states with a name starting with N,
from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    hs = 'localhost'
    DB = MySQLdb.connect(host=hs, user=a[1], passwd=a[2], db=a[3], port=3306)
    C = DB.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id".format(a[4])
    C.execute(query)
    records = C.fetchall()
    for record in records:
        print(record)
    C.close()
    DB.close()
