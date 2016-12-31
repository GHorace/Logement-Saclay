# -*- coding: utf-8 -*-
"""
class definition
"""
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.orm import relationship
from core.db import Base
import core.entities.residents

# Représente la résidence
class Residence:
    pass

# Représente un batiment de la résidence
class Building(Base):
    __tablename__ = 'buildings'
    id = Column(Integer, primary_key=True)
    bundles = relationship("Bundle")
    name = Column(String(32))
    newBuilding = Column(Boolean)

    def getDistanceTo(self, building):
        return 0

# Représente un groupement de chambres (un étage ou une "grappe" de chambres)
class Bundle(Base):
    __tablename__ = 'bundles'
    id = Column(Integer, primary_key=True)
    rooms = relationship("Room")
    building_id = Column(Integer, ForeignKey('buildings.id'))
    name = Column(String(32))

    def getDistanceTo(self, bundle):
        return 0

# Représente une chambre
class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    residents = relationship("Resident")
    bundle_id = Column(Integer, ForeignKey('bundles.id'))
    name = Column(String(32))
    capacity = Column(Integer)
    pricePerResident = Column(Float)

    def getDistanceTo(self, room):
        return 0
