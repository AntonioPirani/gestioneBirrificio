import datetime
import os
import pickle

from Servizio.Prodotto import Prodotto

class Bottiglia(Prodotto):

    def __init__(self):
        super().__init__()
        self.prezzoUnitario = 0.0

    def aggiungiBottiglia(self, tipologia, quantita):
        self.aggiungiProdotto(tipologia, quantita)

        return self

    def rimuoviBottiglia(self, tipologia):
        pass

    def modificaBottiglia(self, tipologia):
        pass

    def registraProdotto(self, tipologia, prezzoUnitario, descrizione='', gradazioneAlcolica=0.0, lotto='', scadenza=datetime.datetime(2022,1,1)):
        self.descrizione = descrizione
        self.gradazioneAlcolica = gradazioneAlcolica
        self.lotto = lotto
        self.scadenza = scadenza
        self.tipologia = tipologia
        self.prezzoUnitario = prezzoUnitario

        prod = {}
        if os.path.isfile('Dati/Prodotti.pickle'):
            with open('Dati/Prodotti.pickle', 'rb') as file:
                prod = pickle.load(file)
                file.close()

        prod[tipologia] = self

        with open('Dati/Prodotti.pickle', 'wb') as file:
            pickle.dump(prod, file, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return f'Bottiglia({self.tipologia}, {self.quantita})'
