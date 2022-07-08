import datetime

from Servizio.Prodotto import Prodotto

class Bottiglia(Prodotto):

    def __init__(self):
        super().__init__()
        self.prezzoUnitario = 0.0

    def aggiungiBottiglia(self, tipologia, quantita, prezzoUnitario=4):
        self.aggiungiProdotto(tipologia, quantita)
        self.prezzoUnitario = prezzoUnitario

        return self

    def rimuoviBottiglia(self, tipologia):
        pass

    def modificaBottiglia(self, tipologia):
        pass

    def __str__(self):
        return f'Bottiglia({self.tipologia}, {self.quantita}, {self.prezzoUnitario})'
