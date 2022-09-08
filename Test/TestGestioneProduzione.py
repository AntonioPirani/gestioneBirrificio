import os
import pickle
import datetime
import unittest
import pandas as pd
from unittest import TestCase

from Attivita.Produzione import Produzione
from Attivita.Materia import Materia
from Servizio.Bottiglia import Bottiglia


class TestGestioneProduzione(unittest.TestCase):

    def testAggiungiProduzione(self):
        materia = Materia().aggiungiMateria(1, 'descrizione', 'lotto', 'Vienna', 10, datetime.datetime(2022, 1, 1))
        prodotto = Bottiglia().aggiungiBottiglia('Giana', 2)
        self.produzione = Produzione().inizioLavorazione(3, materia, prodotto)
        produzioni = None
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
        self.assertIsNotNone(produzioni)
        self.assertIn(3, produzioni)

    def testControllaLavInCorso(self):
        materia1 = Materia().aggiungiMateria(2, 'descrizione', 'lotto', 'Vienna', 1, datetime.datetime(2022, 1, 1))
        prodotto1 = Bottiglia().aggiungiBottiglia('Giana', 5)
        self.produzionePassata = Produzione().inizioLavorazione(10, materia1, prodotto1)
        self.assertTrue(self.produzionePassata.controllaLavInCorso())
        produzioni = None
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                produzioni = pickle.load(f)
        self.assertIsNotNone(produzioni)
        self.assertIn(10, produzioni)









