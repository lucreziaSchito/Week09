from database.dao import Dao

class Model:

    def __init__(self):
        pass


    def get_statistiche(self, serate):
        return Dao.read_statistiche(serate)