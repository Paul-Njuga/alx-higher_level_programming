#!/usr/bin/python3
"""Filter states by user input:

Takes an argument & displays all values in states table of hbtn_0e_0_usa
where name matches argument.
"""
import sys

import MySQLdb


def main():
    """Displays values where name matches state_name"""
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
    cur.execute("SELECT * FROM states WHERE name = {} ORDER BY id ASC", args[4])
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
