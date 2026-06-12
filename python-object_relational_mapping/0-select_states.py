#!/usr/bin/python3
"""
Ce module connecte un script Python à une base de données MySQL
pour lister tous les états de la table 'states'.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Configuration des paramètres de connexion
    host = "localhost"
    port = 3306
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Établissement de la connexion avec la base de données
    db = MySQLdb.connect(
        host=host,
        port=port,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Exécution de la requête SQL pour récupérer les états triés par ID
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    # Affichage des résultats ligne par ligne
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion pour libérer les ressources
    cursor.close()
    db.close()
