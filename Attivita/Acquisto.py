import datetime
import os
import pickle

from Attivita.Ricevuta import Ricevuta


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
        for prodotto in self.elencoProdotti:
            prezzo = self.recuperaPrezzo(prodotto.tipologia)
            iTot += prezzo * prodotto.quantita
            qTot += prodotto.quantita
        self.importoTotale = iTot
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
                #TODO eliminare prenotazione
            else:
                print('Nessuna prenotazione trovata')
        elif elencoProdotti is not None:
            self.elencoProdotti = elencoProdotti
        else:
            return None

        self.calcolaTotale()
        self.dataAcquisto = datetime.datetime.now()

        self.registraAcquisto()
        if aggiorna:
            self.aggiornaQuantita()
        self.rilasciaRicevuta() #TODO


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

    def aggiornaQuantita(self):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))

                #TODO
                for prodotto in inventario.values():
                    if prodotto.tipologia == self.elencoProdotti.tipologia:
                        inventario.quantita -= self.elencoProdotti.quantita

        with open('Dati\Inventario.pickle', 'wb') as f:
            pickle.dump(inventario, f, pickle.HIGHEST_PROTOCOL)

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

    def __str__(self):
        return f'Acquisto({self.codice}, {self.elencoProdotti}, {self.dataAcquisto}, {self.importoTotale}, {self.quantitaTotale})'
