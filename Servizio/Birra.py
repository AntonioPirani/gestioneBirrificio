import datetime

from Servizio.Prodotto import Prodotto

class Birra(Prodotto):

    def __init__(self):
        super().__init__()
        self.prezzoUnitario = 0.0

    def aggiungiBottiglia(self, tipologia, quantita, prezzoUnitario, descrizione='', gradazioneAlcolica=0.0, lotto='', scadenza=datetime.datetime(2022,1,1)):
        self.aggiungiProdotto(tipologia, quantita, descrizione, gradazioneAlcolica, lotto, scadenza)
        self.prezzoUnitario = prezzoUnitario
        pass

    def rimuoviBottiglia(self, tipologia):
        pass

    def modificaBottiglia(self, tipologia):
        pass

    def __str__(self):
        return f'Bottiglia({self.tipologia}, {self.quantita}, {self.prezzoUnitario})'
