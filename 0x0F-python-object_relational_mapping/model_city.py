#!/usr/bin/python3
"""sqlAlchemy class cities module"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """class city definition"""
    __tablename__ = "cities"
    id = Column("id", Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(120), nullable=False)
    state_id = Column("state_id", Integer,
                      ForeignKey("states.id"),
                      nullable=False)
