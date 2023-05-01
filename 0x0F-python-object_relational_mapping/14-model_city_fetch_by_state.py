#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa"""
from model_city import City
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state, city in session\
            .query(State, City)\
            .filter(State.id == City.state_id)\
            .order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()