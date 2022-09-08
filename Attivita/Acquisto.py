import datetime
import os
import pickle
from collections.abc import Iterable

from Attivita.Ricevuta import Ricevuta
from Attivita.Prenotazione import Prenotazione


class Acquisto:

    def __init__(self):
        self.codice = -1
        self.dataAcquisto = datetime.datetime(1970, 1, 1, 0, 0)
        self.elencoProdotti = []
        self.quantitaTotale = 0
        self.importoTotale = 0.0


    def verificaPrenotazione(self, codiceP):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as file:
                prenotazioni = dict(pickle.load(file))
                file.close()

                for prenotazione in prenotazioni.values():
                    if prenotazione.codice == codiceP:
                        return prenotazione
                return None
        else:
            return None


    def calcolaTotale(self):
        iTot = 0.0
        qTot = 0
        if isinstance(self.elencoProdotti, Iterable):
            for prodotto in self.elencoProdotti:
                prezzo = self.recuperaPrezzo(prodotto.tipologia)
                iTot += prezzo * prodotto.quantita
                qTot += prodotto.quantita
        else:
            iTot = self.recuperaPrezzo(self.elencoProdotti.tipologia) * self.elencoProdotti.quantita
            qTot = self.elencoProdotti.quantita
        self.importoTotale = round(iTot, 2)
        self.quantitaTotale = qTot


    def effettuaAcquisto(self, codice, elencoProdotti, codiceP=0): # 0 opzionale
        self.codice = codice
        aggiorna = True

        if codiceP > 0:
            prenotazione = self.verificaPrenotazione(codiceP)
            if prenotazione is not None:
                self.codice = codiceP
                self.elencoProdotti = prenotazione.prodotti
                aggiorna = False
                Prenotazione().rimuoviPrenotazione(codiceP, True)
            else:
                print('Nessuna prenotazione trovata')
                return False
        elif elencoProdotti is not None:
            self.elencoProdotti = elencoProdotti
        else:
            return False

        acquistabile = True
        if aggiorna:

            if isinstance(elencoProdotti, Iterable):
                for elem in elencoProdotti:
                    if self.controllaDisponibilita(elem.tipologia, elem.quantita) and acquistabile:
                        acquistabile = True
                    else:
                        acquistabile = False
            else:
                if self.controllaDisponibilita(elencoProdotti.tipologia, elencoProdotti.quantita):
                    acquistabile = True
                else:
                    acquistabile = False

        if acquistabile:
            self.calcolaTotale()
            self.dataAcquisto = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            self.registraAcquisto()
            if aggiorna:
                if isinstance(self.elencoProdotti, Iterable):
                    for prodotto in self.elencoProdotti:
                        self.aggiornaQuantita(prodotto)
                else:
                    self.aggiornaQuantita(self.elencoProdotti)
            self.rilasciaRicevuta()
            return True
        else:
            return False


    def registraAcquisto(self):
        acquisto = {}
        if os.path.isfile('Dati\Acquisti.pickle'):
            with open('Dati\Acquisti.pickle', 'rb') as f:
                acquisto = pickle.load(f)

        acquisto[self.codice] = self
        with open('Dati\Acquisti.pickle', 'wb') as g:
            pickle.dump(acquisto, g, pickle.HIGHEST_PROTOCOL)

    def visualizzaAcquisto(self, codice):
        if os.path.isfile('Dati\Acquisti.pickle'):
            with open('Dati\Acquisti.pickle', 'rb') as f:
                acquisti = dict(pickle.load(f))
                f.close()
                try:
                    return acquisti[codice]
                except:
                    return None
        else:
            return None

    def ricercaAcquisto(self, codice):
        if os.path.isfile('Dati/Acquisti.pickle'):
            with open('Dati/Acquisti.pickle', 'rb') as f:
                acquisti = dict(pickle.load(f))
                return acquisti.get(codice, None)
        else:
            return None


    def aggiornaQuantita(self, elem):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))

        nome = ''
        for prodotto in inventario.values():
            try:
                if prodotto.tipologia == elem.tipologia:
                    prodotto.quantita = prodotto.quantita - elem.quantita
                    nome = prodotto.tipologia
                    break
            except:
                try:
                    if prodotto.nome == elem.tipologia:
                        prodotto.quantita = prodotto.quantita - elem.quantita
                except:
                    print('AttributeError')
                    return False
        if nome != '':
            inventario[nome] = prodotto
        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario, file, pickle.HIGHEST_PROTOCOL)


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


    def rilasciaRicevuta(self):
        r = Ricevuta()
        r.salvaRicevuta(self.codice, self.dataAcquisto, self.importoTotale, self.elencoProdotti)

    def recuperaPrezzo(self, tipologia):
        if os.path.isfile('Dati\Prodotti.pickle'):
            with open('Dati\Prodotti.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))
                for prodotto in inventario.values():
                    if prodotto.tipologia == tipologia:
                        return prodotto.prezzoUnitario
        return 4.8

    def getInfoAcquisto(self):
        return {
            "codice": self.codice,
            "dataAcquisto": self.dataAcquisto,
            "importoTotale": self.importoTotale,
            "quantitaTotale": self.quantitaTotale,
            "elencoProdotti": self.elencoProdotti,
        }


    def __str__(self):
        return f'Acquisto({self.codice}, {self.elencoProdotti}, {self.dataAcquisto}, {self.importoTotale}, {self.quantitaTotale})'
