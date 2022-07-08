import datetime
import os.path
import pickle
import pandas as pd

class Produzione:

    def __init__(self):
        self.codiceProduzione = -1
        self.dataInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataFine = datetime.datetime(1970, 1, 1, 0, 0)
        self.livello = -1
        self.materieUtilizzate = None
        self.note = ""
        self.prodotto = None
        self.temperatura = -1.0
        self.composto =""


    def inizioLavorazione(self, codiceProduzione):
        self.codiceProduzione = codiceProduzione
        self.dataInizio = datetime.date.today()
        self.dataFine = self.dataInizio + pd.DateOffset(days=1) #la fine della produzione avviene dopo un mese dall'inizio (necessita di scaricarsi il pacchetto dateutil)
        self.livello=1;
        self.temperatura=18.0
        self.composto = "Composto"+str(codiceProduzione)

    def ricercaProduzione(self, codiceProduzione):
        if os.path.isfile('Dati/Produzione.pickle'):
            with open('Dati/Produzione.pickle', 'rb') as f:
                produzioni = pickle.load(f)
                return produzioni[codiceProduzione]
        else:
            return None

    def controllaProdotto(self, codiceProduzione, temperatura, livello, composto, dataInizio, dataFine):

        while dataInizio < dataFine:
            print(temperatura)
            print(livello)
            print(composto)
            dataInizio = dataInizio + pd.DateOffset(hours=4)
            if temperatura > 100 or livello > 2 or composto != "Composto"+codiceProduzione: #i numeri sono a caso
                self.segnalaAnomalia(codiceProduzione)

    def segnalaAnomalia(self, codiceProduzione):
        print("SEGNALATA ANOMALIA")
        self.temperatura = 50
        self.livello = 1
        self.composto="Composto"+codiceProduzione
        return True

    def registraProdotto(self, codiceProduzione, dataInizio, dataFine, livello, materieUtilizzate, note, prodotto, temperatura, composto):
        self.codiceProduzione = codiceProduzione
        self.dataInizio = dataInizio
        self.dataFine = dataFine
        self.livello = livello
        self.materieUtilizzate = materieUtilizzate
        self.note = note
        self.prodotto = prodotto
        self.temperatura = temperatura
        self.composto = composto
        prodotti = {}
        if os.path.isfile('Dati/Produzione.pickle'):
            with open('Dati/Produzione.pickle', 'rb') as f:
                prodotti = pickle.load(f)
        prodotti[codiceProduzione] = self
        with open('Dati/Produzione.pickle', 'wb') as f:
            pickle.dump(prodotti, f, pickle.HIGHEST_PROTOCOL)




    #def aggiornaMagazzino(self, string, temperatura):





