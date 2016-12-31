from sqlalchemy.ext.declarative import declarative_base
from core.entities.typology import *
import core.db as db

engine = db.get_engine()


Base.metadata.create_all(engine)




