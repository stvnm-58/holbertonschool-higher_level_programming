(#!/usr/bin/python3)
"""State class definition and SQLAlchemy Base instance."""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys


Base = declarative_base()


class State(Base):
	"""State model mapped to the "states" table."""
	__tablename__ = 'states'
	id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
	name = Column(String(128), nullable=False)


if __name__ == '__main__':
	# Connect to MySQL on localhost:3306 and create tables.
	# Usage: ./model_state.py <mysql_user> <mysql_password> <db_name>
	if len(sys.argv) != 4:
		print("Usage: {} <mysql_user> <mysql_password> <db_name>".format(sys.argv[0]))
		sys.exit(1)

	user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
	engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
						   .format(user, passwd, db_name))
	Base.metadata.create_all(engine)
