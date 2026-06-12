#!/usr/bin/python3
"""Filtre les états par l'argument fourni, protégé contre les injections SQL."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # Utilisation de %s pour la requête préparée (protection injection SQL)
    # Le mot-clé BINARY force la sensibilité à la casse (Case Sensitivity)
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    
    # On passe la variable dans un tuple (state_name_searched,) à l'execute
    cursor.execute(query, (state_name_searched,))
    
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
