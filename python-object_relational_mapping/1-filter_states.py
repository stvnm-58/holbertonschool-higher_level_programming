#!/usr/bin/python3
"""Liste tous les états commençant par la lettre N majuscule."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Requête SQL avec filtre sur le 'N' majuscule
    query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cursor.execute(query)
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
