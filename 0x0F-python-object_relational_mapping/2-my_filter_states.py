#!/usr/bin/python3
"""Filter states by user input:
Takes an argument & displays all values
in states table of hbtn_0e_0_usa
where name matches argument"""
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
query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
state_name = args[4]
# Pass state_name as tuple not a list, bcs it's one value
cur.execute(query, (state_name,))
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
