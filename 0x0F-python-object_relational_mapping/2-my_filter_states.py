#!/usr/bin/python3
"""Module that lists all states with a name\
    starting with N (upper N) from the database hbtn_0e_0_usa"""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8")

    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM states\
        WHERE name LIKE '{}'\
        ORDER BY states.id ASC".format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
