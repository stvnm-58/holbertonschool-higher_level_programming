#!/usr/bin/python3
"""Liste toutes les villes en argument depuis la base hbtn_0e_4_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    names = [row[0] for row in rows]
    if names:
        print(', '.join(names))

    cursor.close()
    db.close()
