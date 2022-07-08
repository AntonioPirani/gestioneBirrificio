class Consegna:

    def __init__(self):
        self.cliente = None
        self.indirizzo = ''
        self.prodotti = None
        self.ricevuta = None


    def spedisci(self, cliente, indirizzo, prodotti, ricevuta):
        self.cliente = cliente
        self.indirizzo = indirizzo
        self.prodotti = prodotti
        self.ricevuta = ricevuta

        print('Prodotto consegnato')