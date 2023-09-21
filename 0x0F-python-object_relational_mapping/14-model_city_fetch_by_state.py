#!/usr/bin/python3
"""script that prints all City objects from the database"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True))

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(
            City, State.name).join(State).order_by(City.id).all()

    for city, state in cities:
        print('{}: ({}) {}'.format(state, city.id, city.name))

    session.close()