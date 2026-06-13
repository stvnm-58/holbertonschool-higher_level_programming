#!/usr/bin/python3
"""Supprime tous les objets State contenant la lettre 'a'."""
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

    # 1. Sélection et suppression directe en base des états contenant 'a'
    session.query(State).filter(
        State.name.like('%a%')
    ).delete(synchronize_session=False)

    # 2. Validation de la suppression
    session.commit()

    # Fermeture de la session
    session.close()
