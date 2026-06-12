#!/usr/bin/python3
"""Liste toutes les villes de la base de données hbtn_0e_4_usa."""
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

    # Récupération de toutes les villes triées par ID
    query = "SELECT * FROM cities ORDER BY id ASC"
    cursor.execute(query)
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # Fermeture des accès
    cursor.close()
    db.close()
