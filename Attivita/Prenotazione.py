import datetime
import os
import pickle

class Prenotazione:

    def __init__(self):
        self.codice = 0
        self.cliente = None
        self.confermata = False
        self.dataInserimento = datetime.datetime(1970, 1, 1, 0, 0)
        self.importoTotale = 0.0
        self.prodotti = None
        self.quantitaTotale = 0

    def calcolaImporto(self, prodotti):
        tot = 0.0
        for prodotto in prodotti:
            tot += prodotto.getPrezzoUnitario()
        return tot

    def calcolaQuantita(self, prodotti):
        tot = 0
        for prodotto in prodotti:
            tot += prodotto.getQuantita()
        return tot

    def aggiungiPrenotazione(self, codice, cliente, prodotti):
        self.codice = codice
        self.cliente = cliente
        self.dataInserimento = datetime.datetime.now()
        self.prodotti = prodotti
        self.quantitaTotale = self.calcolaQuantita(self, prodotti)
        self.importoTotale = self.calcolaImporto(self, prodotti)

        prenotazione = {}
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as file:
                prenotazione = pickle.load(file)

        prenotazione[codice] = self

        with open('Dati/Prenotazioni.pickle', 'wb') as file:
            pickle.dump(prenotazione, file, pickle.HIGHEST_PROTOCOL)

    def rimuoviPrenotazione(self):


    def modificaPrenotazione(self):


    def visualizzaPrenotazione(self):


    def conferma(self):


    def controllaDisponibilita(self):



