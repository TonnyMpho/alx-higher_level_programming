#!/usr/bin/python3
"""script that adds the State object “Louisiana” to the database"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

if __name__ == '__main__':
    if len(sys.argv) >= 4:
        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]))

        Session = sessionmaker(bind=engine)
        session = Session()

        state = State(name="Louisiana")
        session.add(state)
        session.commit()

        print(state.id)
        session.close()
