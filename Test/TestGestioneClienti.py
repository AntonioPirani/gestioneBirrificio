import os
import pickle
import datetime
from unittest import TestCase

from Attivita.Cliente import Cliente

class TestGestioneClienti(TestCase):

    def testAggiungiCliente(self):
        self.cliente = Cliente()
        self.cliente.aggiungiCliente("informazioni", "tipo", "Test", 123456789, "test@test.com", "Test", datetime.datetime(2001, 11, 22), "Test", "password")
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn("Test", clienti)
    
    def testRimuoviCliente(self):
        clienti = None
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertIn("Test", clienti)
        self.cliente = Cliente().ricercaCliente("Test", "Test")
        self.cliente.rimuoviCliente()
        if os.path.isfile('Dati/Clienti.pickle'):
            with open('Dati/Clienti.pickle', 'rb') as f:
                clienti = pickle.load(f)
        self.assertIsNotNone(clienti)
        self.assertNotIn("Test", clienti)