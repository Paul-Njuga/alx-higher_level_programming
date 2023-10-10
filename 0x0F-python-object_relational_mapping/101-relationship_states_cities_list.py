#!/usr/bin/python3
"""City relationship:

Creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa
"""

if __name__ == "__main__":

    from relationship_state import Base, State
    from relationship_city import City
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .order_by(State.id, State.cities.any().id)\
        .all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    session.close()
