import datetime


class Prodotto:

    def __init__(self):
        self.descrizione = ''
        self.gradazioneAlcolica = 0.0
        self.lotto = ''
        self.scadenza = datetime.datetime(1970, 1, 1)
        self.tipologia = ''
        self.quantita = 0


    def aggiungiProdotto(self, tipologia, quantita, descrizione='', gradazioneAlcolica=0.0, lotto='', scadenza=datetime.datetime(2022,1,1)):
        self.descrizione = descrizione
        self.gradazioneAlcolica = gradazioneAlcolica
        self.lotto = lotto
        self.scadenza = scadenza
        self.tipologia = tipologia
        self.quantita = quantita

        return self
