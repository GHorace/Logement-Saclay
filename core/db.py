import sqlalchemy as sql
import docs.conf as cfg
from sqlalchemy.ext.declarative import declarative_base

# Créer la classe Base qui permet de créer le schema de la base de donnée
# Elle est la classe fille de toute classe dont les objets sont stockés
Base = declarative_base()

_connection = None
_engine = None

# Retourne l'objet engine qui permet d'accéder au moteur qui fait le lien entre le code et la base de donnée
def get_engine():
    global _engine
    if not _engine:
        _engine = sql.create_engine(
            "mysql+mysqlconnector://{}:{}@{}/{}".format(cfg.db["user"], cfg.db["password"], cfg.db["host"],
                                                        cfg.db["database"]))
    return _engine

# Retourne l'objet connection qui permet d'effecture des requetes à la base de données
def get_connection():
    global _connection
    if not _connection:
        _connection = get_engine().connect()
    return _connection
