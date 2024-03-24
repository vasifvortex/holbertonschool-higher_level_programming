#!/usr/bin/python3
"""
Start link class to table in database
"""


from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    if len(argv) != 5:
        return
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state = argv[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(username, password, database),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state_obj = session.query(State).filter(State.name == state).first()

    if state_obj:
        print("{}".format(state_obj.id))
    else:
        print("Not found")

    session.close()


if __name__ == "__main__":
    main()
