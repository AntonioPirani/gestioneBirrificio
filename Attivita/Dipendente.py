


from Attivita.Utilizzatore import Utilizzatore

class Dipendente(Utilizzatore):
    
    def __init__(self):
        super().__init__()
        self.indirizzo = ""

    def aggiungiDipendente(self, indirizzo, nome, telefono, email, cognome, dataNascita, codiceFiscale):
        self.aggiungiUtilizzatore(nome, telefono, email, cognome, dataNascita, codiceFiscale)
        self.indirizzo = indirizzo