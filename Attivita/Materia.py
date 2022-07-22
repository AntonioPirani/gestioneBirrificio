import datetime
import pickle
import os

class Materia:

    def __init__(self):
        self.codice = -1 #non presente sul diagramma delle attivita
        self.descrizione = ""
        self.lotto = ""
        self.nome = ""
        self.quantita = -1
        self.scadenza = datetime.datetime(1970, 1, 1, 0, 0)

    def aggiungiMateria(self, codice, descrizione, lotto, nome, quantita, scadenza):
        self.codice = codice
        self.descrizione = descrizione
        self.lotto = lotto
        self.nome = nome
        self.quantita = quantita
        self.scadenza = scadenza
        materie = {}
        if os.path.isfile('Dati/Materie.pickle'):
            with open('Dati/Materie.pickle', 'rb') as f:
                materie = pickle.load(f)
        materie[codice] = self
        with open('Dati/Materie.pickle', 'wb') as f:
            pickle.dump(materie, f, pickle.HIGHEST_PROTOCOL)

    def ricercaMateria(self, codice):
        if os.path.isfile('Dati/Materie.pickle'):
            with open('Dati/Materie.pickle', 'rb') as f:
                materie = pickle.load(f)
                return materie[codice]
        else:
            return None

    def visualizzaMateria(self, codice):
        self = self.ricercaMateria(codice)
        if os.path.isfile('Dati\Materie.pickle'):
            with open('Dati\Materie.pickle', 'rb') as f:
                materie = dict(pickle.load(f))
                # accesso tramite chiave
                f.close()
                try:
                    print(self)
                    return materie[self.codice]
                except:
                    return None
        else:
            return None

    def visualizzaMateria2(self):
        return {
            "codice": self.codice,
            "descrizione": self.descrizione,
            "lotto": self.lotto,
            "nome": self.nome,
            "quantita": self.quantita,
            "scadenza": self.scadenza,
        }