#!/usr/bin/python3
"""Cities in state:

Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from model_city import City
    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine, asc
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session\
        .query(City.id, City.name, State.name.label('statesId'))\
        .join(State)\
        .order_by(asc(City.id))\
        .all()
    for city in cities:
        print("{}: ({}) {}".format(city.statesId, city.id, city.name))

    session.close()
