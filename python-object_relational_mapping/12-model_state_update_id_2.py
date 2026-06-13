#!/usr/bin/python3
"""Modifie le nom de l'objet State d'ID 2 en 'New Mexico'."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données (Découpage PEP 8)
    db_url = 'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
        username, password, database
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # 1. Récupération de l'état avec l'ID égal à 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # 2. Si l'état existe, on modifie son nom et on commit
    if state_to_update is not None:
        state_to_update.name = "New Mexico"
        session.commit()

    # Fermeture de la session
    session.close()
