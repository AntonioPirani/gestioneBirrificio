import datetime
import os
import pickle


class Ricevuta:
    def __init__(self):
        super(Ricevuta, self).__init__()
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
    def ricercaRicevuta(self,num):
        if os.path.isfile('Dati/Ricevute.pickle'):
            with open('Dati/Ricevute.pickle', 'rb') as f:
                ricevuta = pickle.load(f)
                f.close()
                try:
                    self = ricevuta[num]
                    return self
                except:
                    return None
        return None

    # metodo per la visualizzazione di una ricevuta
    def visualizzaRicevuta(self,num):
        self = self.ricercaRicevuta(num)
        if os.path.isfile('Dati\Ricevute.pickle'):
            with open('Dati\Ricevute.pickle', 'rb') as f:
                ricevuta = pickle.load(f)
                f.close()
                try:
                    print(self)
                    return ricevuta[self.codice]
                except:
                    return None
        else:
            return None

    # metodo per il salvataggio della ricevuta
    def salvaRicevuta(self, codice, dataEmissione, importo, prodotti):
        self.codice = codice
        self.dataEmissione = dataEmissione
        self.importo = importo
        self.prodotti = prodotti

        ricevute = {}
        if os.path.isfile('Dati/Ricevute.pickle'):
            with open('Dati/Ricevute.pickle', 'rb') as file_1:
                ricevute = pickle.load(file_1)
                file_1.close()
        ricevute[codice] = self
        with open('Dati/Ricevute.pickle', 'wb') as file_2:
            pickle.dump(ricevute, file_2, pickle.HIGHEST_PROTOCOL)
            file_2.close()

    def __str__(self):
        return f'Ricevuta({self.codice}, {self.dataEmissione}, {self.importo}, {self.prodotti})'