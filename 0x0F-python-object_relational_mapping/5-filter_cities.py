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
    cur.execute("SELECT cities.name\
                FROM states LEFT JOIN cities\
                ON states.id = cities.state_id\
                WHERE states.name=%s\
                ORDER BY cities.id ASC", (argv[4],))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
