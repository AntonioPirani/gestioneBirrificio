import datetime
import pickle
import os
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
        self.note = ""
        self.dataInizio = datetime.date.today()
        self.dataFine = self.dataInizio + pd.DateOffset(days=1) #la fine della produzione avviene dopo un mese dall'inizio (necessita di scaricarsi il pacchetto dateutil)
        self.livello=1;
        self.temperatura=18.0
        self.composto = "Composto"+str(codiceProduzione)
        produzioni = {}
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
        produzioni[codiceProduzione] = self
        with open('Dati/Produzioni.pickle', 'wb') as f:
            pickle.dump(produzioni, f, pickle.HIGHEST_PROTOCOL)

    def visualizzaProduzione(self):
        return {
            "codiceProduzione": self.codiceProduzione,
            "note": self.note,
            "dataInizio": self.dataInizio,
            "dataFine": self.dataFine,
            "livello": self.livello,
            "temperatura": self.temperatura,
            "comnposto": self.composto,
        }

    def ricercaProduzione(self, codiceProduzione):
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
                return produzioni[codiceProduzione]
        else:
            return None

    def rimuoviProduzione(self):
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
                del produzioni[self.codiceProduzione]
                with open('Dati/Produzioni.pickle', 'wb') as handle:
                    pickle.dump(produzioni, handle, pickle.HIGHEST_PROTOCOL)
                self.codiceProduzione = -1
                self.dataInizio = datetime.datetime(1970, 1, 1, 0, 0)
                self.dataFine = datetime.datetime(1970, 1, 1, 0, 0)
                self.livello = -1
                self.materieUtilizzate = None
                self.note = ""
                self.prodotto = None
                self.temperatura = -1.0
                self.composto = ""
                del self

    def controllaProdotto(self, codiceProduzione, temperatura, livello, composto, dataInizio, dataFine): #meglio chiamare il metodo in controllaProduzione
        while dataInizio <= dataFine:
            #print("Controllo alle ore: "+dataInizio.strftime("%H")+" alla data "+dataInizio.strftime("%Y-%m-%d"))
            dataInizio = dataInizio + pd.DateOffset(hours=4)
            if temperatura > 100 or livello < 2 or composto!="Composto"+str(codiceProduzione): #i numeri sono a caso
                #self.segnalaAnomalia(codiceProduzione)
                print("SEGNALATA ANOMALIA, ")
                temperatura = 50
                livello = 3
                composto = "Composto" + str(codiceProduzione)

    def segnalaAnomalia(self, codiceProduzione): #non funziona
        print("SEGNALATA ANOMALIA, ")
        self.temperatura = 50
        self.livello = 3
        self.composto="Composto"+str(codiceProduzione)

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
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as f:
                prodotti = pickle.load(f)
        prodotti[codiceProduzione] = self
        with open('Dati/Inventario.pickle', 'wb') as f:
            pickle.dump(prodotti, f, pickle.HIGHEST_PROTOCOL)





    #def aggiornaMagazzino(self, string, temperatura):





