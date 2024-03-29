import datetime
import os
import pickle
import unittest

from Attivita.Inventario import Inventario
from Attivita.Materia import Materia

class TestGestioneInventario(unittest.TestCase):
    def testInserimento(self):
        materia = Materia()
        materia.aggiungiMateria(1,"","","Vienna",4,datetime.datetime(1970, 1, 1))
        materie = None
        if os.path.isfile('Dati/Materie.pickle'):
            with open('Dati/Materie.pickle', 'rb') as f:
                materie = pickle.load(f)
        self.assertIsNotNone(materie)
        self.assertIn(1, materie)

    def testAggiornaMagazzino(self):
        inventario = Inventario()
        materia = Materia()
        prima = inventario.ricercaMateria("Vienna")
        materia.aggiungiMateria(2, "", "", "Vienna", 5, datetime.datetime(1970, 1, 1))
        inventario.aggiornaMagazzino(materia)
        aggiornato = None
        if os.path.isfile('Dati/Inventario.pickle'):
            with open('Dati/Inventario.pickle', 'rb') as f:
                aggiornato = pickle.load(f)

        self.assertNotEqual(prima.quantita,inventario.ricercaMateria("Vienna"))
        self.assertIsNotNone(aggiornato)
        self.assertIn("Vienna", aggiornato)

