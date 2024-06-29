#!/usr/bin/python3

"""
This script lists all cities of a state from the database hbtn_0e_0_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    a = sys.argv
    hs = 'localhost'
    DB = MySQLdb.connect(host=hs, user=a[1], passwd=a[2], db=a[3], port=3306)
    C = DB.cursor()
    query1 = "SELECT cities.name "
    query2 = "FROM cities, states "
    query3 = "WHERE cities.state_id = states.id AND states.name = %s "
    query4 = "ORDER BY cities.id"
    C.execute(query1 + query2 + query3 + query4, (a[4],))
    records = C.fetchall()
    cities = [records[i][0] for i in range(len(records))]
    for i in range(len(cities)):
        if i == len(cities) - 1:
            print(cities[i])
        else:
            print(cities[i], end=', ')
    print()
    C.close()
    DB.close()
