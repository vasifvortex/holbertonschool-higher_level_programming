#!/usr/bin/python3
"""Documentation"""


import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    WHERE states.name = %s\
                    ORDER BY cities.id ASC;", (state_name,))
    rows = cursor.fetchall()
    if not rows:
        print()
    else:
        for row in rows:
            if row != rows[-1]:
                print(row[0], end=", ")
            else:
                print(row[0])
    cursor.close()
    db.close()
