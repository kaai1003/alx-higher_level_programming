#!/usr/bin/python3
# SELECT cities AND thier states FROM mysql database
# using forgien key reference
# Usage Script: script_name db_username db_passwrd db_name

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM states \
                JOIN cities \
                ON cities.state_id=states.id \
                ORDER BY cities.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
