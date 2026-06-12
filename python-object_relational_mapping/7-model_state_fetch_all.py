#!/usr/bin/python3
"""Liste tous les objets State de la base de données via SQLAlchemy."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # 1. Création du moteur de connexion (Engine)
    # On utilise 127.0.0.1 pour localhost comme d'habitude
    engine = create_engine(
        'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    # 2. Création de la fabrique de sessions
    Session = sessionmaker(bind=engine)
    
    # 3. Ouverture de la session de travail
    session = Session()

    # 4. Requête ORM : on récupère tous les States triés par id
    states = session.query(State).order_by(State.id).all()

    # 5. Affichage des résultats
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # 6. Fermeture de la session
    session.close()
