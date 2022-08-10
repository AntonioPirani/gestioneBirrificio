import os
import pickle
import unittest

from Attivita.Acquisto import Acquisto
from Servizio.Bottiglia import Bottiglia


class TestGestioneAcquisti(unittest.TestCase):
    def testInserimento(self):
        bottiglia = Bottiglia().aggiungiBottiglia('Giana', 1)
        self.acquisto = Acquisto().effettuaAcquisto(100, bottiglia)
        acquisti = None
        if os.path.isfile('Dati/Acquisti.pickle'):
            with open('Dati/Acquisti.pickle', 'rb') as f:
                acquisti = pickle.load(f)
        self.assertIsNotNone(acquisti)
        self.assertIn(100, acquisti)
        self.assertTrue(self.acquisto)

