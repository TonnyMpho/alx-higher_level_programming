#!/usr/bin/python3
"""script that deletes all State objects with a name
containing the letter 'a' from the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    states_del = session.query(State).filter(State.name.contains('a')).all()

    if states_del:
        for state in states_del:
            session.delete(state)
        session.commit()

    session.close()
