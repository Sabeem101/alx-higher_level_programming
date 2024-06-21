#!/usr/bin/python3
"""
Contains the class definition of a state
and an instance Base.
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    A State class.
    Attributes:
        __tablename__(str): the table name of the class.
        id(int): the state id of the class.
        name(str): the state name of the class.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
