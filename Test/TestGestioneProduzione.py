import os
import pickle
import datetime
import unittest
import pandas as pd
from unittest import TestCase

from Attivita.Produzione import Produzione
from Attivita.Materia import Materia
from Servizio.Prodotto import Prodotto
from Viste.VistaInizioLavorazione import VistaInizioLavorazione


class TestGestioneProduzione(unittest.TestCase):

    def testAggiungiProduzione(self):
        materia = Materia().aggiungiMateria(1, 'descrizione', 'lotto', 'Vienna', 10, datetime.datetime(2022, 1, 1))
        prodotto = Prodotto().aggiungiProdotto('Mezzavalle', 2)
        self.produzione = Produzione().inizioLavorazione(3, materia, prodotto)
        produzioni = None
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
        self.assertIsNotNone(produzioni)
        self.assertIn(3, produzioni)

    def testControllaLavInCorso(self):
        materia1 = Materia().aggiungiMateria(2, 'descrizione', 'lotto', 'Parigi', 10, datetime.datetime(2022, 1, 1))
        prodotto1 = Prodotto().aggiungiProdotto('Mezzavalle', 5)
        self.produzione1 = Produzione().inizioLavorazione(10, materia1, prodotto1)
        self.produzione1.dataInizio = datetime.datetime(2000, 1, 1)
        self.produzione1.dataFine = datetime.datetime(2000, 1, 3)
        materia2 = Materia().aggiungiMateria(3, 'descrizione', 'lotto', 'Monaco', 10, datetime.datetime(2022, 1, 1))
        prodotto2 = Prodotto().aggiungiProdotto('prodotto2', 8)
        self.produzione2 = Produzione().inizioLavorazione(20, materia2, prodotto2)
        produzioni = None
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
        self.assertIsNotNone(produzioni)
        self.assertIn(10, produzioni)
        self.assertIn(20, produzioni)
        self.assertFalse(self.controllaLavInCorso())

    def controllaLavInCorso(self):
        ok = False
        if os.path.isfile('Dati\Produzioni.pickle'):
            with open('Dati\Produzioni.pickle', 'rb') as file0:
                produzioni = dict(pickle.load(file0))
                for produzione in produzioni.values():
                    if produzione.dataFine >= pd.Timestamp(datetime.date.today()):
                        ok = True
            file0.close()
        else:
            ok = False
        return ok




