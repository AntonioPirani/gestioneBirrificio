import datetime

class Materia:

    def __init__(self):
        self.descrizione = ""
        self.lotto = ""
        self.nome = ""
        self.quantita = -1
        self.scadenza = datetime.datetime(1970, 1, 1, 0, 0)