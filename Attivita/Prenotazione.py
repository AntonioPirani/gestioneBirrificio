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
        self.prodotti = []
        self.quantitaTotale = 0

    def calcolaTotale(self):
        iTot = 0.0
        qTot = 0
        for prodotto in self.prodotti:
            prezzo = self.recuperaPrezzo(prodotto.tipologia)
            iTot += prezzo * prodotto.quantita
            qTot += prodotto.quantita
        self.importoTotale = iTot
        self.quantitaTotale = qTot


    def aggiungiPrenotazione(self, codice, cliente, prodotti):
        self.codice = codice
        self.cliente = cliente
        self.dataInserimento = datetime.datetime.now()
        self.prodotti = prodotti
        self.calcolaTotale()

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

    def recuperaPrezzo(self, tipologia):
        if os.path.isfile('Dati\Prodotti.pickle'):
            with open('Dati\Prodotti.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))
                for prodotto in inventario.values():
                    if prodotto.tipologia == tipologia:
                        return prodotto.prezzoUnitario
        return 4.8

    def __str__(self):
        return f'Prenotazione({self.codice}, {self.cliente}, {self.prodotti}, {self.dataInserimento}, {self.importoTotale}, {self.quantitaTotale}, {self.confermata})'
