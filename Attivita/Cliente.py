


from Attivita.Utilizzatore import Utilizzatore

class Cliente(Utilizzatore):

    def __init__(self):
        super().__init__()
        self.informazioni = ""
        self.tipologia = ""

    def aggiungiCliente(self, informazioni, tipologia, nome, telefono, email, cognome, dataNascita, codiceFiscale):
        self.aggiungiUtilizzatore(nome, telefono, email, cognome, dataNascita, codiceFiscale)
        self.informazioni = informazioni
        self.tipologia = tipologia