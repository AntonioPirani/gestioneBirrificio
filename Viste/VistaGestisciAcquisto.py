import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox, QHBoxLayout, QListView
from PyQt5 import QtCore

from Attivita.Acquisto import Acquisto
from Viste.VistaAcquisto import VistaAcquisto
from Viste.VistaEffettuaAcquisto import VistaEffettuaAcquisto

class VistaGestisciAcquisto(QWidget):

    def __init__(self, parent=None):
        super(VistaGestisciAcquisto, self).__init__(parent)
        self.setWindowTitle('Gestione Acquisti')
        layoutVert = QVBoxLayout()
        self.listView = QListView()
        self.updateUI()
        layoutVert.addWidget(self.listView)

        layoutBottoni = QHBoxLayout()
        bottoneApri = QPushButton('Apri')
        bottoneApri.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneApri.clicked.connect(self.mostraInformazioni)
        layoutBottoni.addWidget(bottoneApri)

        bottoneNuovo = QPushButton('Nuovo')
        bottoneNuovo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneNuovo.clicked.connect(self.nuovoAcquisto)
        layoutBottoni.addWidget(bottoneNuovo)

        layoutVert.addLayout(layoutBottoni)
        self.setLayout(layoutVert)
        self.resize(600, 300)

    def nuovoAcquisto(self):
        self.effettuaAcquisto = VistaEffettuaAcquisto(callback=self.updateUI)
        self.effettuaAcquisto.show()

    def mostraInformazioni(self):
        try:
            selected = self.listView.selectedIndexes()[0].data()
            print(selected)
            tipo = selected.split()[7]
            print(tipo)
            codice = int(selected.split()[9])
            print(codice)
            acquisto = None
            if tipo == "Acquisto":
                acquisto = Acquisto().ricercaAcquisto(codice)
                print(acquisto)
            self.vistaAcquisto = VistaAcquisto(acquisto, eliminaCallback=self.updateUI)
            self.vistaAcquisto.show()
        except IndexError:
            print("INDEX ERROR")
            return

    def caricaAcquisti(self):
        if os.path.isfile('Dati/Acquisti.pickle'):
            with open('Dati/Acquisti.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.acquisti.extend(current.values())

    def updateUI(self):
        self.acquisti = []
        self.caricaAcquisti()
        listViewModel = QStandardItemModel(self.listView)
        for acq in self.acquisti:
            item = QStandardItem()
            nome = f"Importo: {acq.importoTotale} € Data: {acq.dataAcquisto} - {type(acq).__name__} Codice: {acq.codice}"
            item.setText(nome)
            item.setEditable(False)
            item.setFont(QFont('Arial', 10))
            listViewModel.appendRow(item)
        self.listView.setModel(listViewModel)
