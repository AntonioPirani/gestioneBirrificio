import datetime
from abc import abstractmethod

class Utilizzatore:

    def __init__(self):
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.email = ""
        self.nome = ""
        self.telefono = 0

    def aggiungiUtilizzatore(self, telefono, nome, email, dataNascita, cognome, codiceFiscale):
        self.codiceFiscale = codiceFiscale
        self.cognome = cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.telefono = telefono

    @abstractmethod
    def ricercaUtilizzatore(nome, cognome):
        pass

    def visualizzaUtilizzatore(self):

        visualizza = ("codiceFiscale: " + self.codiceFiscale + 
                      "cognome: " + self.cognome + 
                      "dataNascita: " + self.dataNascita + 
                      "email:" + self.email + 
                      "nome: " + self.nome + 
                      "telefono: " + self.telefono)
        
        return visualizza

    def rimuoviUtilizzatore(self):
        self.codice = -1
        self.codiceFiscale = ""
        self.cognome = ""
        self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
        self.email = ""
        self.nome = ""
        self.telefono = 0