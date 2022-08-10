import datetime
import os
import pickle
import unittest

from Attivita.Cliente import Cliente
from Attivita.Prenotazione import Prenotazione
from Servizio.Bottiglia import Bottiglia


class TestGestionePrenotazioni(unittest.TestCase):
    def testEliminazione(self):
        prenotazioni = None
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        self.assertIsNotNone(prenotazioni)
        self.assertIn(100, prenotazioni)
        self.prenotazione = Prenotazione()
        self.prenotazione.rimuoviPrenotazione(442509)
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        self.assertIsNotNone(prenotazioni)
        self.assertNotIn(100, prenotazioni)

    def testInserimento(self):
        cliente = Cliente().testCliente('Nessuna', 'Privato', 'Test', 1, 'test', 'Test', datetime.datetime(1970, 1, 1),
                                        'test', 'test')
        bottiglia = Bottiglia().aggiungiBottiglia('Giana', 1)
        self.prenotazione = Prenotazione().aggiungiPrenotazione(100, cliente, bottiglia)
        prenotazioni = None
        if os.path.isfile('Dati/Prenotazioni.pickle'):
            with open('Dati/Prenotazioni.pickle', 'rb') as f:
                prenotazioni = pickle.load(f)
        self.assertIsNotNone(prenotazioni)
        self.assertIn(100, prenotazioni)

    def testControlloDisponibilita(self):
        self.controllo = Prenotazione().controllaDisponibilita('Giana', 1)
        self.assertTrue(self.controllo)
        self.controllo = Prenotazione().controllaDisponibilita('Birra', 1)
        self.assertFalse(self.controllo)
