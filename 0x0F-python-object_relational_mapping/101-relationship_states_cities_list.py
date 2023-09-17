#!/usr/bin/python3
"""script that lists all State objects, and corresponding
City objects, contained in the database"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State, City).join(City).order_by(
            State.id, City.id).all()

    curr_state = ""
    for state, city in states_cities:
        if curr_state == "" or state.id != curr_state.id:
            print('{}: {}'.format(state.id, state.name))
            curr_state = state

        print('     {}: {}'.format(city.id, city.name))

    session.close()
