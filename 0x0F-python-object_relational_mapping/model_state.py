#!/usr/bin/python3
"""sqlAlchemy class state module"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class state definition"""
    __tablename__ = "states"
    id = Column("id", Integer, primary_key=True,
                autoincrement=True, nullable=False)
    name = Column("name", String(120), nullable=False)
