#!/usr/bin/python3
"""add new state to states table
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    session.commit()
    states = session.query(State).filter(State.name == "Louisiana").all()
    for state in states:
        print("{}".format(state.id))
