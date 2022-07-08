import os
import pickle


class Inventario:

    def __init__(self):
        self.materiePrime = None
        self.prodotti = None
        self.quantitaTotaleM = 0
        self.quantitaTotaleP = 0

    #get e set

    def getMateriePrime(self):
        return self.materiePrime
    def setMateriePrime(self,materiePrime):
        self.materiePrime = materiePrime

    def getProtti(self):
        return self.prodotti
    def setProtti(self, prodotti):
        self.prodotti = prodotti

    def getQuantitaTotaleM(self):
        return self.quantitaTotaleM
    def setQuantitaTotaleM(self, quantitaTotaleM):
        self.quantitaTotaleM = quantitaTotaleM

    def getQuantitaTotaleP(self):
        return self.quantitaTotaleP
    def setQuantitaTotaleP(self, quantitaTotaleP):
        self.quantitaTotaleP = quantitaTotaleP

    #metodo per ricercare un prodotto nell'inventario

    def ricercaProdotto(self, nomeProdotto):
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle','rb') as f:
                prodotti = pickle.load(f)
                for prodotto in prodotti.values():
                    if prodotto.nomeProdotto == nomeProdotto:
                        return prodotto
                return None
        else:
            return None

    # metodo per la visualizzazione dell'inventario
    def visualizzaInventario(self):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                inventario = pickle.load(f)
                return inventario
        else:
            return None

    # metodo per aggiornare il magazzino
    def aggiornaMagazzino(self, materiePrime):
        self.materiePrime = materiePrime

        app = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as file:
                app = pickle.load(file)

        app = self
        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(app, file, pickle.HIGHEST_PROTOCOL)