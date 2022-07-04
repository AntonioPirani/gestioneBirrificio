import datetime
import os
import pickle


class Acquisto:

    def __init__(self):
        self.codice = -1
        self.dataAcquisto = datetime.datetime(1970, 1, 1, 0 , 0)
        self.elencoProdotti = None
        self.quantitaTotale = 0
        self.importoTotale = 0.0


    def verificaPrenotazione(self, codiceP):
        if os.path.isfile('Dati\Prenotazioni.pickle'):
            with open('Dati\Prenotazioni.pickle', 'rb') as f:
                prenotazioni = dict(pickle.load(f))

                try:
                    if not prenotazioni[codiceP]:
                        return None
                    else:
                        return prenotazioni[codiceP]
                except:
                    return None
