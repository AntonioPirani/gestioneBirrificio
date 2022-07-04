import datetime
import os
import pickle


class Ricevuta:
    def __init__(self):
        self.codice =  0
        self.dataEmissione = datetime.datetime(1970, 1, 1, 0, 0)
        self.importo = 0.0
        self.prodotti = None

        # get e set

        def getCodice(self):
            return self.Codice
        def setCodice(self, Codice):
            self.Codice = Codice

        def getDataEmissione(self):
            return self.DataEmissione
        def setDataEmissione(self, DataEmissione):
            self.DataEmissione = DataEmissione

        def getImporto(self):
            return self.Importo
        def setImporto(self, Importo):
            self.Importo = Importo

        def getImporto(self):
            return self.Importo
        def setImporto(self, Importo):
            self.Importo = Importo

        def getProdotti(self):
            return self.Prodotti
        def setImporto(self, Prodotti):
            self.Prodotti = Prodotti

        # metodo per la ricerca di una ricevuta
        def ricercaRicevuta(self, num):
            if os.path.isfile('Dati/Ricevuta.pickle'):
                with open('Dati/Ricevuta.pickle', 'rb') as f:
                    ricevuta = pickle.load(f)
                    return ricevuta[num]
            else:
                return None

        # metodo per la visualizzazione di una ricevuta
        def visualizzaRicevuta(self):
            if os.path.isfile('Dati\Ricevuta.pickle'):
                with open('Dati\Ricevuta.pickle', 'rb') as f:
                    ricevuta = dict(pickle.load(f))
                    try:
                        return ricevuta[self.codice]
                    except:
                        return None
            else:
                return None