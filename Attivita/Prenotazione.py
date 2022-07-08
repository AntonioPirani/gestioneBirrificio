import datetime
import os
import pickle

class Prenotazione:

    def __init__(self, prodotti):
        self.codice = 0
        self.cliente = None
        self.confermata = False
        self.dataInserimento = datetime.datetime(1970, 1, 1, 0, 0)
        self.importoTotale = 0.0
        self.prodotti = prodotti
        self.quantitaTotale = 0


    def calcolaImporto(self):
        tot = 0.0
        for prodotto in self.prodotti:
            tot += prodotto.prezzoUnitario
        return tot


    def calcolaQuantita(self, prodotti):
        tot = 0
        for prodotto in prodotti:
            tot += prodotto.quantita
        return tot


    def aggiungiPrenotazione(self, codice, cliente, prodotti):
        self.codice = codice
        self.cliente = cliente
        self.dataInserimento = datetime.datetime.now()
        self.prodotti = prodotti
        self.quantitaTotale = self.calcolaQuantita(prodotti)
        self.importoTotale = self.calcolaImporto()

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


    def modificaPrenotazione(self, prodotti, codice):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))

                self.prodotti = prodotti
                self.quantitaTotale = self.calcolaQuantita(self)
                self.importoTotale = self.calcolaImporto(self)
                prenotazione[codice] = self

        with open('Dati\Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)


    def ricercaPrenotazione(self, codice):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                f.close()
                try:
                    self = prenotazioni[codice]
                    return self
                except:
                    return None
        return None


    def visualizzaPrenotazione(self, codice):
        self = self.ricercaPrenotazione(codice)
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))
                #accesso tramite chiave
                f.close()
                try:
                    print(self)
                    return prenotazioni[self.codice]
                except:
                    return None
        else:
            return None


    def conferma(self, codice):
        self = self.ricercaPrenotazione(codice)
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))
                self.confermata = True
                prenotazione[self.codice] = self

        with open('Dati\Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)


    def controllaDisponibilita(self, tipologia, quantita):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))
                for prodotto in inventario.values():
                    if prodotto.tipologia == tipologia and prodotto.quantita > quantita:
                        return True
        return False

    def __str__(self):
        return f'Prenotazione({self.codice}, {self.cliente}, {self.prodotti}, {self.dataInserimento}, {self.importoTotale}, {self.quantitaTotale}, {self.confermata})'
