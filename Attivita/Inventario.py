import os
import pickle


class Inventario:

    def __init__(self):
        self.materiePrime = []
        self.prodotti = []
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
        inventario_m = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as file:
                inventario_m = dict(pickle.load(file))

        for materia in inventario_m.values():
            if materia.materiePrime.nome == materiePrime.nome:
                #aggiungere un elemento alla volta quando si richiama il metodo
                self.materiePrime.quantita = materia.materiePrime.quantita + materiePrime.quantita
        inventario_m[materiePrime.nome] = self

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario_m, file, pickle.HIGHEST_PROTOCOL)
        print(inventario_m)


    def calcolaQuantitaM(self):
        pass

    def calcolaQuantitaP(self):
        pass

    def __str__(self):
        return f'Inventario({self.materiePrime})'