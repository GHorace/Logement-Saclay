from sqlalchemy.ext.declarative import declarative_base
from core.entities.typology import *
import core.db as db
from core.db import Base

engine = db.get_engine()

Base.metadata.create_all(engine)