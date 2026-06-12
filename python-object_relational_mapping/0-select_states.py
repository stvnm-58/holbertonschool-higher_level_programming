#!/usr/bin/python3
"""
Ce module connecte un script Python à une base de données MySQL
pour lister tous les états de la table 'states'.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Établissement de la connexion avec la base de données
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()


    for row in rows:
        print(row)

    cursor.close()
    db.close()
