from tkinter import messagebox
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
        self.layout.addWidget(self.label, 0, 0, 1, 5)


        self.label1 = QLabel("Materia", self)
        self.label2 = QLabel("Quantità", self)
        self.label3 = QLabel("Prodotto", self)

        self.comboBox = QComboBox(self)
        self.spinBox = QSpinBox(self)
        self.comboBox2 = QComboBox(self)
        self.spinBox2 = QSpinBox(self)

        self.button = QPushButton("Inizia Lavorazione")

        self.layout.addWidget(self.label3, 1, 0, 1, 1)
        self.layout.addWidget(self.label1, 2, 0, 1, 1)
        self.layout.addWidget(self.label2, 1, 2, 1, 1)
        self.layout.addWidget(self.label2, 2, 2, 1, 1)

        self.layout.addWidget(self.comboBox2, 1, 1, 1, 2)
        self.layout.addWidget(self.comboBox, 2, 1, 1, 2)
        self.layout.addWidget(self.spinBox, 1, 3, 1, 2)
        self.layout.addWidget(self.spinBox2, 2, 3, 1, 2)

        self.layout.addWidget(self.button, 4, 4, 1, 1)

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
        if not self.getMateria():
            self.close()
        else:
            self.produzione.inizioLavorazione(self.getCodice(), self.getMateria(), self.getProdotto()) 
            print(self.produzione.visualizzaProduzione)
            msgbox = QMessageBox()
            msgbox.setText("Lavorazione iniziata con successo")
            msgbox.exec()
            self.close()
    
    def getProdotto(self):
        prodotto = Prodotto()
        prodotto.tipologia = self.comboBox2.currentText()
        prodotto.quantita = self.spinBox.value()
        return prodotto

    def getMateria(self):
        materia = Materia()
        materia.nome = self.comboBox.currentText()
        materia.quantita = self.spinBox2.value()

        if not self.controllaDisponibilita(materia.nome, materia.quantita): 
            msgbox = QMessageBox()
            msgbox.setText("Materia insufficiente")
            msgbox.exec()
            return False
        else: 
            return materia

    def getCodice(self):
        i = 1
        if os.path.isfile('Dati\Produzioni.pickle'):
            with open('Dati\Produzioni.pickle', 'rb') as file0:
                produzioni = dict(pickle.load(file0))
                for produzione in produzioni.values():
                        if produzione.codiceProduzione == i:
                            i = i+1
            file0.close()
            codice = i
        else:
            codice = 1

        return codice
        

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