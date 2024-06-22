#!/usr/bin/python3
"""
Defines the State class and a Base instance.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base


class City(Base):
    """
    The City class.
    Attributes:
        __tablename__(str): the class' table name.
        id(int): the class' id.
        name(str): the class' name.
        state_id(int): the state that the city belongs to.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
