import pickle
import os

from Attivita.Utilizzatore import Utilizzatore

class Dipendente(Utilizzatore):
    
    def __init__(self):
        super().__init__()
        self.indirizzo = ""

    def aggiungiDipendente(self, indirizzo, nome, telefono, email, cognome, dataNascita, codiceFiscale): #codice
        self.aggiungiUtilizzatore(telefono, nome, email, dataNascita, cognome, codiceFiscale) #codice
        self.indirizzo = indirizzo
        dipendenti = {}
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as f:
                dipendenti = pickle.load(f)
        dipendenti[codiceFiscale] = self
        with open('Dati/Dipendenti.pickle', 'wb') as f:
            pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)

    def ricercaDipendente(self, nome, cognome):
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                for dipendente in dipendenti.values():
                    if dipendente.nome == nome and dipendente.cognome == cognome:
                        return dipendente
                return None
        else:
            return None

    def rimuoviDipendente(self):
        if os.path.isfile('Dati/Dipendenti.pickle'):
            with open('Dati/Dipendenti.pickle', 'rb') as f:
                dipendenti = dict(pickle.load(f))
                del dipendenti[self.codiceFiscale]
            with open('Dati/Dipendenti.pickle', 'wb') as f:
                pickle.dump(dipendenti, f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.indirizzo = ""
        del self

    def visualizzaDipendente(self):
        visualizza = self.visualizzaUtilizzatore()
        visualizza["indirizzo"] = self.indirizzo
        return visualizza