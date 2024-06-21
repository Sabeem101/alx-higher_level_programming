#!/usr/bin/python3
"""
Adds the state 'Louisiana' to the database.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    Connects to the database
    to add a new state.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Session = sessionmaker(bind=engine)
    ses = Session()
    louis = State(name='Louisiana')
    ses.add(louis)
    ses.commit()
    print('{0}'.format(louis.id))
    ses.close()
