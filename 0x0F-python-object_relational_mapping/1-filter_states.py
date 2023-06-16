#!/usr/bin/python3
"""Filter states:
Lists all states with name
starting with upper N from hbtn_0e_0_usa"""
import sys

import MySQLdb

args = sys.argv
conn = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=args[1],
    passwd=args[2],
    db=args[3],
    charset="utf8",
)
cur = conn.cursor()
query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
cur.execute(query)
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
