#!/usr/bin/python3
"""Get a state:

Prints the State object with the name passed as argument
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
    
    arg = argv[4]
    state = session.query(State).filter_by(name=arg).order_by(State.id).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
