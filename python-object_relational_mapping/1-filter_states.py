#!/usr/bin/python3
"""Liste tous les états de la table 'states'."""
import sys
import MySQLdb

if __name__ == "__main__":
    # On vérifie que les 3 arguments requis sont bien présents
    if len(sys.argv) >= 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Connexion à la base de données
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        cursor = db.cursor()
        
        # Exécution et récupération
        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        rows = cursor.fetchall()

        # Affichage
        for row in rows:
            print(row)

        # Fermeture des connexions
        cursor.close()
        db.close()
