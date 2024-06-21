#!/usr/bin/python3
"""
Changes the name of a State object
from the database 'hbtn_0e_6_usa'.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv

if __name__ == '__main__':
    """
    Updates the id of a state object in the database.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Session = sessionmaker(bind=engine)
    ses = Session()
    aris = ses.query(State).filter(State.id == '2').first()
    aris.name = 'New Mexico'
    ses.commit()
    ses.close()
