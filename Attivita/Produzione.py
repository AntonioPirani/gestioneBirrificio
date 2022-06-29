import datetime
import os.path
import pickle
#from dateutil.relativedelta import relativedelta

class Produzione:

    def __init__(self):
        self.codiceProduzione = -1
        self.dataInizio = datetime.datetime(1970, 1, 1, 0, 0)
        self.dataFine = datetime.datetime(1970, 1, 1, 0, 0)
        self.livello = -1
        self.materieUtilizzate = None
        self.note = ""
        self.prodotto = None
        self.temperatura = -1

    #get e set del codice non presente sul diagramma delle classi
    def getCodiceProduzione(self):
        return self.codiceProduzione
    def setCodiceProduzione(self, codiceProduzione):
        self.codiceProduzione = codiceProduzione

    def getDataInizio(self):
        return self.dataInizio
    def setDataInizio(self, dataInizio):
        self.dataInizio = dataInizio

    def getDataFine(self):
        return self.DataFine
    def setDataFine(self, dataFine):
        self.dataFine = dataFine

    def getLivello(self):
        return self.livello
    def setLivello(self, livello):
        self.livello = livello

    def getMaterieUtilizzate(self):
        return self.materieUtilizzate
    def setMaterieUtilizzate(self, materieUtilizzate):
        self.materieUtilizzate = materieUtilizzate

    def getNote(self):
        return self.note
    def setNote(self, note):
        self.note = note

    def getProdotto(self):
        return self.prodotto
    def setNote(self, prodotto):
        self.prodotto = prodotto

    def getTemperatura(self):
        return self.temperatura
    def setTemperatura(self, temperatura):
        self.temperatura = temperatura

    def inizioLavorazione(self, materieUtilizzate): #materieUtilizzate da aggiungere nel diagramma delle classi -> inizioLavorazione(Materia)
        # print("Quale tipo di materia prima necessiti?")
        #tipologia=input()
        #if tipologia non presente in materieUtilizzate

        self.codiceProduzione = 0 # non va bene
        self.dataInizio = datetime.date.today()
        #self.dataFine = self.dataInizio + relativedelta(months=1) #la fine della produzione avviene dopo un mese dall'inizio (necessita di scaricarsi il pacchetto dateutil)
        self.livello=0;
        self.temperatura=18.0
        #self.prodotto= Prodotto()

    def ricercaProduzione(self, codiceProduzione):
        if os.path.isfile('Dati/Produzione.pickle'):
            with open('Dati/Produzione.pickle', 'rb') as f:
                produzioni = pickle.load(f)
                return produzioni[codiceProduzione]
        else:
            return None

    def controllaProdotto(self, Prodotto, temperatura, livello):
        #while prodotto in lavorazione
        self.getTemperatura
        self.getLivello
        #il composto?
        if temperatura > 100 or livello > 2: # i numeri sono a caso
            self.segnalaAnomalia(temperatura, livello)


    def segnalaAnomalia(self, temperatura, livello):
        print("SEGNALATA ANOMALIA")
        self.temperatura = 50
        self.livello = 1
        #composto?
        return True

    #def registraProdotto(self, prodotto):

    #def aggiornaMagazzino(self, note, temperatura):





