#!/usr/bin/python3

"""
Python module that contains the class definition of a State.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import declarative_base


Base = declarative_base()


class State(Base):
    """
    A tables that describes states.
    """
    __table_name__ = 'states'

    id = Column(Integer, autoincrement=True,
                unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
