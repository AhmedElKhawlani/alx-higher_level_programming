#!/usr/bin/python3

"""
Python Module to list all City objects from the database.
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(argv[1], argv[2],
                argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sess = Session()
    results = sess.query(City, State).filter(City.state_id == State.id).all()
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    sess.commit()
    sess.close()
