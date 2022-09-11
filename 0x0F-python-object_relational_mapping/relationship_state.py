#!/usr/bin/python3
""" contains the class definition of a State and an instance """
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")
