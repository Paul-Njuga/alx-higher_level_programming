#!/usr/bin/python3
"""All cities by state:

Takes a state name as argument,
and lists all cities of that state,
using the database hbtn_0e_4_usa.
"""


def main():
    """Lists all cities by states"""
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
        state_name = args[4]
        query = "SELECT cities.name\
                FROM cities\
                INNER JOIN states\
                ON cities.state_id=states.id\
                WHERE states.name LIKE BINARY %s\
                ORDER BY cities.id ASC"
        cur.execute(query, (state_name,))
        query_rows = cur.fetchall()
        print(", ".join([row[0] for row in query_rows]))  # List comprehension


if __name__ == "__main__":
    main()
