import datetime

from Servizio.Prodotto import Prodotto

class Bicchiere(Prodotto):

    def __init__(self):
        super().__init__()
        self.capacita = 0.0
        self.prezzo = 0.0

    def aggiungiBicchiere(self, tipologia, quantita, capacita, prezzo, descrizione='', gradazioneAlcolica=0.0, lotto='', scadenza=datetime.datetime(2022,1,1)):
        self.aggiungiProdotto(tipologia, quantita, descrizione, gradazioneAlcolica, lotto, scadenza)
        self.capacita = capacita
        self.prezzo = prezzo
        pass

    def rimuoviBicchiere(self, tipologia):
        pass

    def modificaBicchiere(self, tipologia):
        pass

    def __str__(self):
        return f'Bicchiere({self.tipologia}, {self.quantita}, {self.capacita}, {self.prezzo})'
