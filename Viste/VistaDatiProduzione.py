import os.path
import pickle

#import current as current
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox, QHBoxLayout, QListView
from PyQt5 import QtCore

from Attivita.Produzione import Produzione

class VistaDatiProduzione(QWidget):

    def __init__(self, parent=None):
        super(VistaDatiProduzione, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.list_view = QListView()
        self.aggiorna_produzione()
        self.layout.addWidget(self.list_view)

        self.resize(400, 300)
        self.setWindowTitle("Gestore Birrificio")
        self.setLayout(self.layout)
        self.show()

    def getButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet('background-color: rgba(255, 153, 0);'
                             'font: 75 14pt "Arial";color: rgb(255, 255, 127);')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def load_produzioni(self):
        if os.path.isfile('Dati/Produzioni.pickle'):
            with open('Dati/Produzioni.pickle', 'rb') as f:
                current = dict(pickle.load(f))
                self.produzioni.extend(current.values())

    def aggiorna_produzione(self):
        self.produzioni = []
        self.load_produzioni()
        listview_model = QStandardItemModel(self.list_view)
        for produzione in self.produzioni:
            item = QStandardItem()
            dati = f" {produzione.dataInizio} fine: {produzione.dataFine} - {produzione.temperatura} {produzione.livello} {produzione.composto}"
            item.setText(dati)
            item.setEditable(False)
            font = item.font()
            font.setPointSize(18)
            item.setFont(font)
            listview_model.appendRow(item)
        self.list_view.setModel(listview_model)

    #stampa produzioni nel pickle
