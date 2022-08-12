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
        # for materia in inventario_m.values():
        #     #materia.materiePrime.nome
        #     if materia.nome == materiePrime.nome:
        #         #aggiungere un elemento alla volta quando si richiama il metodo
        #         self.materiePrime.quantita = materia.quantita + materiePrime.quantita

        self.materiePrime = materiePrime
        inventario_m = {}
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as file:
                inventario_m = dict(pickle.load(file))
                file.close()

        print(type(materiePrime).__name__)
        for materia in inventario_m.values():
            try:
                if materia.nome == materiePrime.nome:
                    self.materiePrime.quantita = materia.quantita + materiePrime.quantita
            except:
                try:
                    if materia.tipologia == materiePrime.nome:
                        #self.materiePrime.quantita = materia.quantita + materiePrime.quantita
                        print("Bottiglia")
                except:
                    print('AttributeError')

        inventario_m[self.materiePrime.nome] = self.materiePrime

        with open('Dati/Inventario.pickle', 'wb') as file:
            pickle.dump(inventario_m, file, pickle.HIGHEST_PROTOCOL)
        print(inventario_m)


    def calcolaQuantitaM(self):
        pass

    def calcolaQuantitaP(self):
        pass

    def __str__(self):
        return f'Inventario({self.materiePrime})'