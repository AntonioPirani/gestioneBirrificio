from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox, QSizePolicy, QMessageBox

from Attivita.Cliente import Cliente
from datetime import datetime


class VistaClienti(QWidget):
    
    def __init__(self, parent=None):
        super(VistaClienti, self).__init__(parent)

        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.label = QLabel("Aggiungi Cliente", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 3)

        self.label1 = QLabel("Nome", self)
        self.label2 = QLabel("Cognome", self)
        self.label3 = QLabel("Data Nascita", self)
        self.label4 = QLabel("Codice Fiscale", self)
        self.label5 = QLabel("Telefono", self)
        self.label6 = QLabel("Tipologia", self)
        self.label7 = QLabel("Informazioni", self)

        self.lineedit1 = QLineEdit(self)
        self.lineedit2 = QLineEdit(self)
        self.lineedit3 = QLineEdit(self)
        self.lineedit4 = QLineEdit(self)
        self.lineedit5 = QLineEdit(self)
        self.lineedit6 = QComboBox(self)
        self.lineedit7 = QLineEdit(self)

        self.button = QPushButton("Registrati")

        self.layout.addWidget(self.label1, 1, 0, 1, 1)
        self.layout.addWidget(self.label2, 2, 0, 1, 1)
        self.layout.addWidget(self.label3, 3, 0, 1, 1)
        self.layout.addWidget(self.label4, 4, 0, 1, 1)
        self.layout.addWidget(self.label5, 5, 0, 1, 1)
        self.layout.addWidget(self.label6, 6, 0, 1, 1)
        self.layout.addWidget(self.label7, 7, 0, 1, 1)

        self.layout.addWidget(self.lineedit1, 1, 1, 1, 2)
        self.layout.addWidget(self.lineedit2, 2, 1, 1, 2)
        self.layout.addWidget(self.lineedit3, 3, 1, 1, 2)
        self.layout.addWidget(self.lineedit4, 4, 1, 1, 2)
        self.layout.addWidget(self.lineedit5, 5, 1, 1, 2)
        self.layout.addWidget(self.lineedit6, 6, 1, 1, 2)
        self.layout.addWidget(self.lineedit7, 7, 1, 1, 2)

        self.layout.addWidget(self.button, 8, 2, 1, 1)

        self.lineedit6.addItem("Privato")
        self.lineedit6.addItem("Azienda")


        self.button.clicked.connect(self.aggiungiCliente)


        self.resize(400, 350)
        self.setWindowTitle("Vista Clienti")
        self.setLayout(self.layout)
        self.show()

    def aggiungiCliente(self):
        print("Evviva")