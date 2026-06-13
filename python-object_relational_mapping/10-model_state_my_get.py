#!/usr/bin/python3
"""Affiche l'ID de l'état passé en argument depuis la base hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name_searched = sys.argv[4]

    # Connexion à la base de données
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête avec filtre sur le nom exact de l'état
    # .first() renvoie le premier objet trouvé ou None s'il n'y a pas de correspondance
    state = session.query(State).filter(State.name == state_name_searched).first()

    # Affichage du résultat selon les contraintes de l'énoncé
    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    # Fermeture de la session
    session.close()
