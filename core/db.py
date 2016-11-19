import sqlalchemy as sql
import docs.conf as cfg
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

_connection = None
_engine = None


def get_engine():
    global _engine
    if not _engine:
        _engine = sql.create_engine(
            "mysql+mysqlconnector://{}:{}@{}/{}".format(cfg.db["user"], cfg.db["password"], cfg.db["host"],
                                                        cfg.db["database"]))
    return _engine


def get_connection():
    global _connection
    if not _connection:
        _connection = get_engine().connect()
    return _connection
