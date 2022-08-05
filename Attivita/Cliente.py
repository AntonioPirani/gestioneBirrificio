import pickle
import os

from Attivita.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.informazioni = ""
        self.tipologia = ""

    def aggiungiCliente(self, informazioni, tipologia, nome, telefono, email, cognome, dataNascita, codiceFiscale): #codice
        self.aggiungiUtilizzatore(telefono, nome, email, dataNascita, cognome, codiceFiscale) #codice
        self.informazioni = informazioni
        self.tipologia = tipologia
        clienti = {}
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        #clienti[codice] = self
        clienti[codiceFiscale] = self
        with open('Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def ricercaCliente(self, nome, cognome):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome == nome and cliente.cognome == cognome:
                        return cliente
                return None
        else:
            return None

    def rimuoviCliente(self):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                del clienti[self.codiceFiscale]
            with open('Dati/Clienti.pickle', 'wb') as f:
                pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.informazioni = ""
        self.tipologia = ""
        del self

    def visualizzaCliente(self):
        visualizza = self.visualizzaUtilizzatore()
        visualizza["informazioni"] = self.informazioni
        visualizza["tipologia"] = self.tipologia
        return visualizza

    def autenticaCliente(self, codice, password):
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.codiceFiscale == codice and cliente.password == password:
                        self = cliente
                        return self
                        #return cliente?
                return False
        else:
            return False
