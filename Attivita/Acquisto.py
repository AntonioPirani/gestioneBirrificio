import datetime
import os
import pickle


class Acquisto:

    def __init__(self):
        self.codice = -1
        self.dataAcquisto = datetime.datetime(1970, 1, 1, 0, 0)
        self.elencoProdotti = []
        self.quantitaTotale = 0
        self.importoTotale = 0.0


    def verificaPrenotazione(self, codiceP):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
<<<<<<< HEAD
            with open('Dati\Prenotazioni.pickle', 'rb') as file:
                prenotazioni = dict(pickle.load(file))
                file.close()

                for prenotazione in prenotazioni.values():
                    if prenotazione.codice == codiceP:
                        return prenotazione
                return None
        else:
            return None


    def calcolaImporto(self):
        tot = 0.0
        for prodotto in self.elencoProdotti:
            tot += prodotto.getPrezzoUnitario()
        self.importoTotale = tot


    def calcolaQuantita(self):
        tot = 0
        for prodotto in self.elencoProdotti:
            tot += prodotto.getQuantita()
        self.quantitaTotale = tot


    def effettuaAcquisto(self, codice, elencoProdotti, codiceP=0): # 0 opzionale
        self.codice = codice

        if codiceP > 0:
            prenotazione = self.verificaPrenotazione(codiceP)
            if prenotazione is not None:
                self.elencoProdotti = prenotazione.prodotti
            else:
                print('Nessuna prenotazione trovata')
        elif elencoProdotti is not None:
            self.elencoProdotti = elencoProdotti
        else:
            return None

        self.importoTotale()
        self.quantitaTotale()
        self.dataAcquisto = datetime.datetime.now()

        self.registraAcquisto(codice)
        #for prodotto in elencoProdotti:
        #    self.aggiornaQuantita(prodotto.tipologia, prodotto.quantita)


    def registraAcquisto(self, codice):
        acquisto = {}
        if os.path.isfile('Dati\Acquisti.pickle'):
            with open('Dati\Acquisti.pickle', 'rb') as f:
                acquisto = pickle.load(f)

        acquisto[codice] = self
        with open('Dati\Acquisti.pickle', 'wb') as g:
            pickle.dump(acquisto, g, pickle.HIGHEST_PROTOCOL)


    def aggiornaQuantita(self, tipologia, quantita):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = dict(pickle.load(f))

                #TODO
                #for prodotto in inventario.values():
                #    if prodotto.tipologia == tipologia:
                #        inventario[quantita] -= quantita
                #        #inventario.quantita -= quantita
                inventario[tipologia] -= quantita

        with open('Dati\Inventario.pickle', 'wb') as f:
            pickle.dump(inventario, f, pickle.HIGHEST_PROTOCOL)


    def __str__(self):
        return f'Acquisto({self.codice}, {self.elencoProdotti}, {self.dataAcquisto}, {self.importoTotale}, {self.quantitaTotale})'
=======
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))

                try:
                    if not prenotazioni[codiceP]:
                        return None
                    else:
                        return prenotazioni[codiceP]
                except:
                    return None
>>>>>>> parent of be961d3 (Merge remote-tracking branch 'origin/master')
