#!/usr/bin/python3
"""
Lists all State objects
from the database hbtn_0e_6_use.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    Connects to the database and gets the states
    from the database.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Session = sessionmaker(bind=engine)
    ses = Session()

    for instance in ses.query(State).order_by(State.id):
        print('{0}: {1}'.format(instance.id, instance.name))
