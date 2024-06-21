#!/usr/bin/python3
"""
Prints all city objects from the database 'hbtn_0e_14_usa'.
"""
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sys import argv

if __name__ == '__main__':
    """
    Connects to the database and gets the cities
    from the database.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Session = sessionmaker(bind=engine)
    ses = Session()
    quer = ses.query(City, State).join(State)

    for C, S in quer.all():
        print("{}: ({:d}) {}".format(S.name, C.id, C.name))
    ses.commit()
    ses.close()
