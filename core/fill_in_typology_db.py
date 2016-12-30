import core.db as db
from sqlalchemy.orm import sessionmaker
from core.entities.typology import *

engine = db.get_engine()
conn = db.get_connection()
Session = sessionmaker(bind=engine)



def get_buildings():
    session = Session()
    wb = xlrd.open_workbook("../docs/Buildings.xlsx")
    feuilles = wb.sheet_names()
    feuille_i = wb.sheet_by_name(feuilles[0])
    colonne_1 = feuille_i.col_values(0)
    colonne_2 = feuille_i.col_values(1)
    colonne_3 = feuille_i.col_values(2)
    for i in range(1,len(colonne_1)):
        (bundles,name,newBuilding)=(list(colonne_1[i]),str(colonne_2[i]),bool(colonne_3[i]))
        session.add(Building(bundle=bundles,name=name,newBuilding=newBuilding))
    session.commit()

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
        (rooms,building_id,building,name)=(list(colonne_1[i]),str(colonne_2[i]),bool(colonne_3[i]),str(colonne_4[i]))
        session.add(Bundle(rooms=rooms,building_id=building_id,building=building,neme=name))
    session.commit()

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
        (residents,bundle_id,bundle,name,capacity,pricePerResident)=(list(colonne_1[i]),int(colonne_2[i]),str(colonne_3[i]),str(colonne_4[i]),int(colonne_5[i]),float(colonne_6[i]))
        session.add(Room(residents=residents,bundle_id=bundle_id,bundle=bundle,name=name,capacity=capacity,pricePerResident=pricePerResident))
    session.commit()









