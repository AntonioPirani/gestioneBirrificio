import datetime
import os
import pickle
from collections.abc import Iterable


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
        if isinstance(self.prodotti, Iterable):
            for prodotto in self.prodotti:
                prezzo = self.recuperaPrezzo(prodotto.tipologia)
                iTot += prezzo * prodotto.quantita
                qTot += prodotto.quantita
        else:
            iTot = self.recuperaPrezzo(self.prodotti.tipologia)
            qTot = self.prodotti.quantita
        self.importoTotale = iTot
        self.quantitaTotale = qTot


    def aggiungiPrenotazione(self, codice, cliente, prodotti):

        prenotabile = True
        if isinstance(prodotti, Iterable):
            for elem in prodotti:
                if self.controllaDisponibilita(elem.tipologia, elem.quantita) and prenotabile:
                    prenotabile = True
                else:
                    prenotabile = False
        else:
            if self.controllaDisponibilita(prodotti.tipologia, prodotti.quantita):
                prenotabile = True
            else:
                prenotabile = False

        if prenotabile:
            self.codice = codice
            self.cliente = cliente
            self.dataInserimento = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.prodotti = prodotti
            self.calcolaTotale()

            prenotazione = {}
            if os.path.isfile('Dati/Prenotazioni.pickle'):
                with open('Dati/Prenotazioni.pickle', 'rb') as file:
                    prenotazione = pickle.load(file)

            prenotazione[codice] = self

            with open('Dati/Prenotazioni.pickle', 'wb') as file:
                pickle.dump(prenotazione, file, pickle.HIGHEST_PROTOCOL)
            return True

        else:
            return False


    def rimuoviPrenotazione(self, codice):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f1:
                prenotazioni = dict(pickle.load(f1))
                del prenotazioni[codice]
                f1.close()
            with open('Dati\Prenotazioni.pickle', 'wb') as f2:
                pickle.dump(prenotazioni, f2, pickle.HIGHEST_PROTOCOL)

            if self.confermata is True:
                if isinstance(self.prodotti, Iterable):
                    for elem in self.prodotti:
                        self.riassegnaQuantita(elem)
                else:
                    self.riassegnaQuantita(self.prodotti)

            self.codice = 0
            self.cliente = None
            self.confermata = False
            self.dataInserimento = datetime.datetime(1970, 1, 1, 0, 0)
            self.importoTotale = 0.0
            self.prodotti = []
            self.quantitaTotale = 0
            del self


    def modificaPrenotazione(self, codice, cliente, prodotti):
        # if os.path.isfile('Dati\Prenotazioni.pickle'):
        #     with open('Dati\Prenotazioni.pickle', 'rb') as f:
        #         prenotazione = dict(pickle.load(f))
        #
        #         self.prodotti = prodotti
        #         self.calcolaTotale()
        #         prenotazione[codice] = self
        #
        # with open('Dati\Prenotazioni.pickle', 'wb') as f:
        #     pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)
        self.aggiungiPrenotazione(codice, cliente, prodotti)


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
        prenotazione = {}
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazione = dict(pickle.load(f))

                if self.confermata is True:
                    return False

                if isinstance(self.prodotti, Iterable):
                    for elem in self.prodotti:
                        check = self.controllaDisponibilita(elem.tipologia, elem.quantita)
                        if check is not True:
                            return False
                else:
                    check = self.controllaDisponibilita(self.prodotti.tipologia, self.prodotti.quantita)
                    if check is not True:
                        return False

                if check:
                    self.confermata = True
                    prenotazione[self.codice] = self

                    if isinstance(self.prodotti, Iterable):
                        for elem in self.prodotti:
                            self.riservaQuantita(elem)
                    else:
                        self.riservaQuantita(self.prodotti)

                else:
                    return False

        with open('Dati\Prenotazioni.pickle', 'wb') as f:
            pickle.dump(prenotazione, f, pickle.HIGHEST_PROTOCOL)
        return True


    def controllaDisponibilita(self, tipologia, quantita):
        ok = False
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as file0:
                inventario = dict(pickle.load(file0))
                for prodotto in inventario.values():
                    try:
                        if prodotto.tipologia == tipologia and prodotto.quantita > quantita:
                            ok = True
                    except:
                        try:
                            if prodotto.nome == tipologia and prodotto.quantita > quantita:
                                ok = True
                        except:
                            print('AttributeError')
                            ok = False
        file0.close()
        return ok

    def recuperaPrezzo(self, tipologia):
        if os.path.isfile('Dati\Prodotti.pickle'):
            with open('Dati\Prodotti.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))
                for prodotto in inventario.values():
                    if prodotto.tipologia == tipologia:
                        return prodotto.prezzoUnitario
        return 4.8

    def riservaQuantita(self, elem):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))

        for prodotto in inventario.values():
            try:
                if prodotto.tipologia == elem.tipologia:
                    elem.quantita = prodotto.quantita - elem.quantita
            except:
                try:
                    if prodotto.nome == elem.tipologia:
                        elem.quantita = prodotto.quantita - elem.quantita
                except:
                    print('AttributeError')
                    return False

        inventario[elem.tipologia] = elem

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario, file, pickle.HIGHEST_PROTOCOL)


    def riassegnaQuantita(self, elem):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))

        for prodotto in inventario.values():
            try:
                if prodotto.tipologia == elem.tipologia:
                    elem.quantita = prodotto.quantita + elem.quantita
            except:
                try:
                    if prodotto.nome == elem.tipologia:
                        elem.quantita = prodotto.quantita + elem.quantita
                except:
                    print('AttributeError')
                    return False

        inventario[elem.tipologia] = elem

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario, file, pickle.HIGHEST_PROTOCOL)

    def __str__(self):
        return f'Prenotazione({self.codice}, {self.cliente}, {self.prodotti}, {self.dataInserimento}, {self.importoTotale}, {self.quantitaTotale}, {self.confermata})'
