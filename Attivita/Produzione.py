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

    def inizioLavorazione(self, codiceProduzione, Materia, Prodotto):
        self.codiceProduzione = codiceProduzione
        self.note = ""
        self.dataInizio = datetime.date.today()
        self.dataFine = self.dataInizio + pd.DateOffset(days=1) #la fine della produzione avviene dopo un giorno dall'inizio (necessita di scaricarsi il pacchetto dateutil)
        self.livello=1;
        self.temperatura=18.0
        self.composto = "Composto"+str(codiceProduzione)

        self.materieUtilizzate = Materia.aggiungiMateria(10, "descr", "3n", "Monaco", 1, datetime.datetime(2022, 7, 30)) #aggiungimaterie
        self.aggiornaMagazzinoMaterie(self.materieUtilizzate) #rimovi materie utilizzate

        self.prodotto = Prodotto.aggiungiProdotto("Monaco", 20) #aggiungo prodotto
        self.registraProdotto(codiceProduzione) #registro prodotto
        self.aggiornaMagazzinoProdotti(self.prodotto)#aggiorna prodotto

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
            print("Controllo alle ore: "+dataInizio.strftime("%H")+" alla data "+dataInizio.strftime("%Y-%m-%d"))
            dataInizio = dataInizio + pd.DateOffset(hours=4)
            if temperatura > 50 or livello < 2 or composto != "Composto" + str(codiceProduzione):
                self.segnalaAnomalia(codiceProduzione)
            else:
                print("nessun problema")



    def segnalaAnomalia(self, codiceProduzione):
        print("SEGNALATA ANOMALIA ")
        self.setTemeperatura(20)
        self.setLivello(3)
        self.setComposto("Composto" + str(codiceProduzione))



    def registraProdotto(self, codiceProduzione):
        self.codiceProduzione = codiceProduzione
        prodotti = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as f:
                prodotti = pickle.load(f)
        prodotti[codiceProduzione] = self
        with open('Dati/Inventario.pickle', 'wb') as f:
            pickle.dump(prodotti, f, pickle.HIGHEST_PROTOCOL)

    def aggiornaMagazzinoMaterie(self, materieRimosse):
        self.materieRimosse = materieRimosse
        inventario_m = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as file:
                inventario_m = dict(pickle.load(file))

        for materia in inventario_m.values():
            if materia.nome == materieRimosse.nome :
                if materia.quantita - materieRimosse.quantita >=0:
                    self.materiePrime.quantita = materia.quantita - materieRimosse.quantita
                else:
                    return False

        inventario_m[materieRimosse.nome] = self.materieUtilizzate

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario_m, file, pickle.HIGHEST_PROTOCOL)
        print(inventario_m)

    def aggiornaMagazzinoProdotti(self, prodottoAggiunto):
        self.prodottoAggiunto = prodottoAggiunto
        inventario_m = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as file:
                inventario_m = dict(pickle.load(file))

        for prodotto in inventario_m.values():
            if prodotto.tipologia == prodottoAggiunto.tipologia:
                # aggiungere un elemento alla volta quando si richiama il metodo
                self.prodottoAggiunto.quantita = prodotto.quantita + prodottoAggiunto.quantita
        inventario_m[prodottoAggiunto.tipologia] = self.prodottoAggiunto

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario_m, file, pickle.HIGHEST_PROTOCOL)
        print(inventario_m)

    def getTemepratura(self):
        return self.temepratura
    def setTemeperatura(self,temperatura):
        self.temepratura = temperatura

    def getLivello(self):
        return self.livello
    def setLivello(self, livello):
        self.livello = livello

    def getComposto(self):
        return self.composto
    def setComposto(self, composto):
        self.composto = composto