#!/usr/bin/python3
"""Ajoute l'objet State 'Louisiana' à la base de données hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données
    db_url = 'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
        username, password, database
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Création de la nouvelle instance de State
    new_state = State(name="Louisiana")

    # 2. Ajout de l'objet à la session
    session.add(new_state)

    # 3. Validation de la transaction pour insérer la ligne en BDD
    session.commit()

    # 4. Affichage de l'ID généré automatiquement par MySQL
    print("{}".format(new_state.id))

    # Fermeture de la session
    session.close()
