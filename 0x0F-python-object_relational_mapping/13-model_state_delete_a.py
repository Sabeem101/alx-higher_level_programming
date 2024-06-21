#!/usr/bin/python3
"""
Deletes all state objects with a name containing the letter
'a' from the database 'hbtn_0e_6_usa'.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    Deletes all states containing the letter 'a'
    from the database.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Session = sessionmaker(bind=engine)
    ses = Session()

    STATES = ses.query(State).filter(State.name.like('%a%')).all()
    [ses.delete(state) for state in STATES]
    ses.commit()
