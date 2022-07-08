import datetime
import os
import pickle


class Prodotto:

    def __init__(self):
        self.descrizione = ''
        self.gradazioneAlcolica = 0.0
        self.lotto = ''
        self.scadenza = datetime.datetime(1970, 1, 1)
        self.tipologia = ''
        self.quantita = 0

    def aggiungiProdotto(self, tipologia, quantita):
        self.tipologia = tipologia
        self.quantita = quantita

        return self

    def rimuoviProdotto(self, tipologia):
        pass

    def modificaProdotto(self, tipologia):
        pass

    def registraProdotto(self, tipologia, descrizione='', gradazioneAlcolica=0.0, lotto='', scadenza=datetime.datetime(2022,1,1)):
        self.descrizione = descrizione
        self.gradazioneAlcolica = gradazioneAlcolica
        self.lotto = lotto
        self.scadenza = scadenza
        self.tipologia = tipologia

        prod = {}
        if os.path.isfile('Dati/Prodotti.pickle'):
            with open('Dati/Prodotti.pickle', 'rb') as file:
                prod = pickle.load(file)
                file.close()

        prod[tipologia] = self

        with open('Dati/Prodotti.pickle', 'wb') as file:
            pickle.dump(prod, file, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return f'Prodotto({self.tipologia}, {self.quantita})'
