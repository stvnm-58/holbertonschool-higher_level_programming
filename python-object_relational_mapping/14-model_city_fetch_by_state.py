#!/usr/bin/python3
"""Liste tous les objets City de la base de données hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connexion à la base de données (Formatage PEP 8)
    db_url = 'mysql+mysqldb://{}:{}@127.0.0.1:3306/{}'.format(
        username, password, database
    )
    engine = create_engine(db_url, pool_pre_ping=True)

    # Création de la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Requête de jointure triée par l'ID des villes
    results = session.query(City, State).\
        filter(City.state_id == State.id).\
        order_by(City.id.asc()).\
        all()

    # Affichage des résultats au format : <state name>: (<city id>) <city name>
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Fermeture de la session
    session.close()
