from core.entities.typology import *
from core.db import *

class RandomRooming:


    def initialize(self):
        db = get_connection()
        self.users = db.execute()

    def compute(self):
        pass