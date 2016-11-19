# -*- coding: utf-8 -*-
"""
class definition
"""
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from core.db import Base

class Building(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True)
    bundles = relationship("Bundle", back_populates="building")

class Bundle(Base):
    __tablename__ = 'bundles'
    id = Column(Integer, primary_key=True)
    rooms = relationship("Room", back_populates="bundle")
    building_id = Column(Integer, ForeignKey('buildings.id'))
    building = relationship("Building", back_populates="bundles")

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    residents = relationship("Resident", back_populates="room")
    bundle_id = Column(Integer, ForeignKey('bundles.id'))
    bundle = relationship("Bundle", back_populates="rooms")

class Resident(Base):
    __tablename__ = 'residents'
    id = Column(Integer, primary_key=True)
    room_id = Column(Integer, ForeignKey('rooms.id'))
    room = relationship("Room", back_populates="residents")

class Residence:
    pass
