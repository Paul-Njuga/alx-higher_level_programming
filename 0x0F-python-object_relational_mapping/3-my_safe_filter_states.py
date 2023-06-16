#!/usr/bin/python3
"""SQL Injection:

Takes an argument & displays all values in states table of hbtn_0e_0_usa
where name matches argument & is safe from MySQL injections.
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
        query = "SELECT * FROM states\
                WHERE name LIKE BINARY %s\
                ORDER BY id ASC"
        state_name = args[4]
        # Pass state_name as a tuple not a list, bcs its a single value
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)


if __name__ == "__main__":
    main()
