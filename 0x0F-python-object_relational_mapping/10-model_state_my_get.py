#!/usr/bin/python3

"""
Python Module liste a state by his name.
"""
from sys import argv
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
    session = Session()
    found = False
    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print(state.id)
            found = True
    if not found:
        print("Not found")
    session.close()
