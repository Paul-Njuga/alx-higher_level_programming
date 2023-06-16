#!/usr/bin/python3
"""Filter states by user input:

Takes an argument & displays all values in states table of hbtn_0e_0_usa
where name matches argument.
"""


def main():
    """Displays values where name matches state_name"""
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
        # No argument validation
        cur.execute(
            "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(
                args[4]
            )
        )
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)


if __name__ == "__main__":
    main()
