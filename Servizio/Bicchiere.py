import datetime

from Servizio.Prodotto import Prodotto

class Bicchiere(Prodotto):

    def __init__(self):
        super().__init__()
        self.capacita = 0.0
        self.prezzo = 0.0

    def aggiungiBicchiere(self, tipologia, quantita, capacita, prezzo):
        self.aggiungiProdotto(tipologia, quantita)
        self.capacita = capacita
        self.prezzo = prezzo

        return self

    def rimuoviBicchiere(self, tipologia):
        pass

    def modificaBicchiere(self, tipologia):
        pass

    def __str__(self):
        return f'Bicchiere({self.tipologia}, {self.quantita}, {self.capacita}, {self.prezzo})'
