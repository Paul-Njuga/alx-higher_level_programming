#!/usr/bin/python3
"""Definition of City class"""

from model_state import Base
from sqlalchemy import ForeignKey, Column, Integer, String


class City(Base):
    """Class City"""
    __tablename__ = 'cities'
    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
