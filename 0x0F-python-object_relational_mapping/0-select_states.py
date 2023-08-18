#!/usr/bin/python3
"""
Get all states:
Lists all states from hbtn_0e_0_usa.
"""


def main():
    """Lists all states"""
    from sys import argv as args
    import MySQLdb

    with MySQLdb.connect(
        host="localhost",
        port=3306,
        user=args[1],
        passwd=args[2],
        db=args[3],
        charset="utf8",
    ) as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)


if __name__ == "__main__":
    main()
