#!/usr/bin/python3
"""script to list all states that start with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states WHERE name REGEXP "^[N]"')
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
