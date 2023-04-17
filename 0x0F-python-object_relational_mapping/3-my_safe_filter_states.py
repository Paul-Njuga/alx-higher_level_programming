#!/usr/bin/python3
"""A script that takes in an argument and displays all values\
    in the states table of hbtn_0e_0_usa where name matches the argument\
        and is SQL injection free."""
"""Always use placeholders even for numbers and other non-string values\
    so that the database can fill in the data values properly and safely."""

if __name__ == '__main__':

    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2],
        db=argv[3], charset="utf8")

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name=%s\
                ORDER BY states.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
