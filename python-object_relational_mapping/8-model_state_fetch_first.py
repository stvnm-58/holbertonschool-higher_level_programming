#!/usr/bin/python3
"""Affiche le premier objet State de la base de données hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données avec SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Création de la session de travail
    Session = sessionmaker(bind=engine)
    session = Session()

    # Récupération du premier State trié par id (.first() limite la requête SQL à 1 résultat)
    first_state = session.query(State).order_by(State.id).first()

    # Affichage du résultat selon les contraintes de l'énoncé
    if first_state is not None:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    # Fermeture de la session
    session.close()
