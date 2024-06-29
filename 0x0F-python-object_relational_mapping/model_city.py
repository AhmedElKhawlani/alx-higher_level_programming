#!/usr/bin/python3

"""
Python module that contains the class definition of a City.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """
    A tables that describes cities.
    """
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
