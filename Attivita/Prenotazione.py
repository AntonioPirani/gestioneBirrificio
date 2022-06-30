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


    def calcolaImporto(self):
        tot = 0.0
        for prodotto in self.prodotti:
            tot += prodotto.getPrezzoUnitario()
        return tot


    def calcolaQuantita(self):
        tot = 0
        for prodotto in self.prodotti:
            tot += prodotto.getQuantita()
        return tot


    def aggiungiPrenotazione(self, codice, cliente, prodotti):
        self.codice = codice
        self.cliente = cliente
        self.dataInserimento = datetime.datetime.now()
        self.prodotti = prodotti
        self.quantitaTotale = self.calcolaQuantita(self)
        self.importoTotale = self.calcolaImporto(self)

        prenotazione = {}
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as file:
                prenotazione = pickle.load(file)

        prenotazione[codice] = self

        with open('Dati/Prenotazioni.pickle', 'wb') as file:
            pickle.dump(prenotazione, file, pickle.HIGHEST_PROTOCOL)


    def rimuoviPrenotazione(self):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'wb+') as f:
                prenotazioni = pickle.load(f)
                del prenotazioni[self.codice]
                pickle.dump(prenotazioni, f, pickle.HIGHEST_PROTOCOL)
            self.codice = 0
            self.cliente = None
            self.confermata = False
            self.dataInserimento = datetime.datetime(1970, 1, 1, 0, 0)
            self.importoTotale = 0.0
            self.prodotti = None
            self.quantitaTotale = 0
            del self


    def modificaPrenotazione(self, prodotti):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'wb+') as f:
                prenotazione = dict(pickle.load(f))

                self.prodotti = prodotti
                self.quantitaTotale = self.calcolaQuantita(self)
                self.importoTotale = self.calcolaImporto(self)

                prenotazione[self.codice] = self
                pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)

    def visualizzaPrenotazione(self):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                # accesso tramite chiave
                try:
                    return prenotazioni[self.codice]
                except:
                    return None
        else:
            return None


    def conferma(self):
        self.confermata = True


    def controllaDisponibilita(self):



