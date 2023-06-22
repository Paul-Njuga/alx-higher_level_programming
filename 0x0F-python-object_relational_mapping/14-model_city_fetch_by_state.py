#!/usr/bin/python3
"""Cities in state:

Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""
import sys

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session\
        .query(City.id, City.name, State.name.label('stateId'))\
        .join(State)\
        .filter(City.state_id == State.id)\
        .order_by(City.id)\
        .all()
    for city in cities:
        print("{}: ({}) {}".format(city.stateId, city.id, city.name))
    session.close()
