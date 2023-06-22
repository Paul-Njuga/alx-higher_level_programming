#!/usr/bin/python3
"""Delete states:

Deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from model_state import Base, State
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

    for state in session.query(State).filter(State.name.like("%a%")):
        session.delete(state)

    session.commit()
    session.close()
