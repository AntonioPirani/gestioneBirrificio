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
        if os.path.isfile('Dati/InventarioProdotto.pickle'):
            with open('Dati/InventarioProdotto.pickle','rb') as f:
                prodotti = pickle.load(f)
                for prodotto in prodotti.values():
                    if prodotto.nomeProdotto == nomeProdotto:
                        return prodotto
                return None
        else:
            return None

    # metodo per la visualizzazione dell'inventario
    def visualizzaInventario(self):
        if os.path.isfile('Dati\InventarioMaterie.pickle'):
            with open('Dati\InventarioMaterie.pickle', 'rb') as f:
                inventario = pickle.load(f)
                f.close()
                try:
                    print(self)
                    return inventario
                except:
                    return None
        else:
            return None

    # metodo per aggiornare il magazzino
    def aggiornaMagazzino(self, materiePrime):
        self.materiePrime = materiePrime
        agg = {}
        if os.path.isfile('Dati/InventarioMaterie.pickle'):
            with open('Dati/InventarioMaterie.pickle', 'rb') as file:
                agg = dict(pickle.load(file))
                for materia in agg.values():
                    if materia.nome == materiePrime.nome:
                        with open('Dati/InventarioMaterie.pickle', 'wb') as file:
                            materia.quantita = materia.quantita + materiePrime.quantita
                            app = self
                            pickle.dump(agg, file, pickle.HIGHEST_PROTOCOL)
                        return True

    """def calcolaQuantitaM
        tot = 0
        for materia in materiePrime:
            tot += materia.quantita
        return tot

    def calcolaQuantitaP
        tot = 0
        for prodotto in prodotti:
            tot += prodotto.quantita
        return tot"""

    def __str__(self):
        return f'InventarioMaterie({self.materiePrime})'