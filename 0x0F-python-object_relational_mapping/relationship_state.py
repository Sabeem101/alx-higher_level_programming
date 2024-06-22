#!/usr/bin/python3
"""
Defines a State class and a Base class
to work with MySQLAlchemy ORM.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    The State class.
    Attributes:
        __tablename__(str): the class' table name.
        id(int): the class' state id.
        name(str): the class' state name.
        cities(:obj:'City'): the cities belonging to the state.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
