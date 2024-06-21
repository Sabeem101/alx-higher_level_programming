#!/usr/bin/python3
"""
Contains a definition for the City class.
"""
from sqlalchemy import Column, Integer, ForeignKey, String
from model_state import Base, State


class City(Base):
    """
    The City class.
    Attributes:
        __tablename__(str): the city's table name.
        id(int): the city's id.
        name(str): the city's name.
        state_id(int): the state that contains the city.
    """
    __tablename__ = 'cities'
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    id = Column(Integer, primary_key=True)
