#!/usr/bin/python3
"""Cities by states:

Lists all cities from the database hbtn_0e_4_usa.
"""


def main():
    """Lists all cities"""
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
        query = "SELECT cities.id, cities.name, states.name\
                FROM cities\
                INNER JOIN states ON cities.id=states.id\
                ORDER BY cities.id ASC"
        cur.execute(query)
        query_rows = cur.fetchall()
        for row in query_rows:
            print(row)


if __name__ == "__main__":
    main()
