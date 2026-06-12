#!/usr/bin/python3
"""Liste toutes les villes d'un état passé en argument depuis la base hbtn_0e_4_usa."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    query = (
        "SELECT cities.id, cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name LIKE BINARY %s "
        "ORDER BY cities.id ASC"
    )
    
    cursor.execute(query, (state_name,))
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
