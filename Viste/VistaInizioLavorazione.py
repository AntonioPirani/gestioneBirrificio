from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QComboBox, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox, QSpinBox
from PyQt5 import QtCore

import pickle
import os

from Attivita.Produzione import Produzione
from Servizio.Prodotto import Prodotto
from Attivita.Materia import Materia

class VistaInizioLavorazione(QWidget):

    def __init__(self, parent=None):
        super(VistaInizioLavorazione, self).__init__(parent)

        self.label = QLabel("Area Inizio Lavorazione", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 4)


        self.label1 = QLabel("Materia", self)
        self.label2 = QLabel("Quantità", self)
        self.label3 = QLabel("Prodotto", self)

        self.comboBox = QComboBox(self)
        self.spinBox = QSpinBox(self)
        self.comboBox2 = QComboBox(self)

        self.button = QPushButton("Inizia Lavorazione")

        self.layout.addWidget(self.label3, 1, 0, 1, 1)
        self.layout.addWidget(self.label1, 2, 0, 1, 1)
        self.layout.addWidget(self.label2, 3, 0, 1, 1)

        self.layout.addWidget(self.comboBox2, 1, 1, 1, 2)
        self.layout.addWidget(self.comboBox, 2, 1, 1, 2)
        self.layout.addWidget(self.spinBox, 3, 1, 1, 2)

        self.layout.addWidget(self.button, 4, 0, 1, 1)

        self.comboBox.addItem("Vienna")
        self.comboBox.addItem("Monaco")

        self.comboBox2.addItem("Papola")
        self.comboBox2.addItem("Mezzavalle")

        self.button.clicked.connect(self.iniziaLavorazione)
        
        self.prodotto = None
        self.materia = None

        self.resize(400, 350)
        self.setWindowTitle("Vista Inizio Lavorazione")
        self.setLayout(self.layout)
        self.show()

    def iniziaLavorazione(self):
        self.produzione = Produzione()
        self.produzione.inizioLavorazione(1, self.getMateria(), self.getProdotto()) 
        print(self.produzione.visualizzaProduzione())
        print("Inizia la lavorazione")

    
    def getProdotto(self):
        prodotto = Prodotto()
        prodotto.tipologia = self.comboBox2.currentText()
        prodotto.quantita = 1
        return prodotto

    def getMateria(self):
        materia = Materia()
        materia.nome = self.comboBox.currentText()
        materia.quantita = self.spinBox.value()
        return materia

    def controllaDisponibilita(self, tipologia, quantita):
        ok = False
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as file0:
                inventario = dict(pickle.load(file0))
                for materia in inventario.values():
                    try:
                        if materia.tipologia == tipologia and materia.quantita > quantita:
                            ok = True
                    except:
                        try:
                            if materia.nome == tipologia and materia.quantita > quantita:
                                ok = True
                        except:
                            print('AttributeError')
                            ok = False
        file0.close()
        return ok

    #def getQuantita(self):
        #return self.spinBox.value()