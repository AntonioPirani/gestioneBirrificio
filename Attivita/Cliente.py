import pickle
import os


from Attivita.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.informazioni = ""
        self.tipologia = ""

    def aggiungiCliente(self, informazioni, tipologia, nome, telefono, email, cognome, dataNascita, codiceFiscale, codice):
        self.aggiungiUtilizzatore(nome, telefono, email, cognome, dataNascita, codiceFiscale, codice)
        self.informazioni = informazioni
        self.tipologia = tipologia
        clienti = {}
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        clienti[codice] = self
        with open('Dati/Clienti.pickle', 'wb') as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)