# -*- coding: utf-8 -*-
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base

# Représente un résident
class Resident(Base):
    __tablename__ = 'residents'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship("Room", back_populates="residents")


# Représente une réponse au questionnaire
class TestEntry(Base):
    __tablename__ = 'test_entries'
    id = Column(Integer, primary_key=True)
