#!/usr/bin/python3
"""Liste tous les états de la table 'states'."""
import sys
import MySQLdb

if __name__ == "__main__":
    # Récupération des arguments de la ligne de commande
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données MySQL locale
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Création du curseur et exécution de la requête SQL
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    # Affichage de chaque ligne du résultat
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
