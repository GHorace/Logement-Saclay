from sqlalchemy.ext.declarative import declarative_base
from core.entities.typology import *
from core.entities.residents import  *
import core.db as db

engine = db.get_engine()


Base.metadata.create_all(engine)




