#!/usr/bin/python3
"""
Creates the state 'California' with the city 'San Francisco'
from the database 'hbtn_0e_100_usa'.
"""
from relationship_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from relationship_city import City
from sys import argv

if __name__ == '__main__':
    """
    Connects to the database
    to add a new state and city.
    """
    eng_db = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
    engine = create_engine(eng_db)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    ses = Session()
    cali = State(name='California')
    sancity = City(name='San Francisco')
    cali.cities.append(sancity)
    ses.add(cali)
    ses.commit()
    ses.close()
