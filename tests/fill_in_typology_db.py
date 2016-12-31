# -*- coding: utf-8 -*-

import core.db as db
from sqlalchemy.orm import sessionmaker
from core.entities.typology import *
import xlrd
import core.excel.excel_conv as conv

engine = db.get_engine()
Session = sessionmaker(bind=engine)

# Remplit la table "rooms" à partir des données de Rooms.xlsx
def get_rooms():
    session = Session()
    wb = xlrd.open_workbook("../docs/Rooms.xlsx")
    feuilles = wb.sheet_names()
    feuille_i = wb.sheet_by_name(feuilles[0])
    colonne_1 = feuille_i.col_values(0)
    colonne_2 = feuille_i.col_values(1)
    colonne_3 = feuille_i.col_values(2)
    colonne_4 = feuille_i.col_values(3)
    colonne_5 = feuille_i.col_values(4)
    colonne_6 = feuille_i.col_values(5)
    for i in range(1,len(colonne_1)):
        (id,residents,bundle_id,name,capacity,pricePerResident)=(int(colonne_1[i]),conv.strToList(colonne_2[i]),int(colonne_3[i]),str(colonne_4[i]),int(colonne_5[i]),float(colonne_6[i]))
        session.add(Room(id=id,residents=residents,bundle_id=bundle_id,name=name,capacity=capacity,pricePerResident=pricePerResident))
    session.commit()

# Remplit la table "bundles" à partir des données de Bundles.xlsx
def get_bundles():
    session = Session()
    wb = xlrd.open_workbook("../docs/Bundles.xlsx")
    feuilles = wb.sheet_names()
    feuille_i = wb.sheet_by_name(feuilles[0])
    colonne_1 = feuille_i.col_values(0)
    colonne_2 = feuille_i.col_values(1)
    colonne_3 = feuille_i.col_values(2)
    colonne_4 = feuille_i.col_values(3)
    for i in range(1,len(colonne_1)):
        rooms_list=[session.query(Room).get(k) for k in conv.strToList(colonne_2[i])]
        (id,rooms,building_id,name)=(int(colonne_1[i]),rooms_list,int(colonne_3[i]),str(colonne_4[i]))
        session.add(Bundle(id=id,rooms=rooms,building_id=building_id,name=name))
    session.commit()


# Remplit la table "Buildings" à partir des données de Buildings.xlsx
def get_buildings():
    session = Session()
    wb = xlrd.open_workbook("../docs/Buildings.xlsx")
    feuilles = wb.sheet_names()
    feuille_i = wb.sheet_by_name(feuilles[0])
    colonne_1 = feuille_i.col_values(0)
    colonne_2 = feuille_i.col_values(1)
    colonne_3 = feuille_i.col_values(2)
    colonne_4 = feuille_i.col_values(3)
    for i in range(1, len(colonne_1)):
        bundles_list = [session.query(Bundle).get(k) for k in conv.strToList(colonne_2[i])]
        (id, bundles, name, newBuilding) = (int(colonne_1[i]), bundles_list, str(colonne_3[i]), conv.strToBool(colonne_4[i]))
        session.add(Building(id=id, bundles=bundles, name=name, newBuilding=newBuilding))
    session.commit()


# clean et remplit les tables "rooms", "bundles" et "buildings"
def fill_in_db():
    session = Session()
    session.query(Room).delete()
    session.query(Bundle).delete()
    session.query(Building).delete()
    session.commit()
    get_rooms()
    get_bundles()
    get_buildings()

fill_in_db()




