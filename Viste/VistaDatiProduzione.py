from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore

from Viste.VistaInizioLavorazione import VistaInizioLavorazione

class VistaDatiProduzione(QWidget):

    def __init__(self, parent=None):
        super(VistaDatiProduzione, self).__init__(parent)

        self.label = QLabel("Area Dati Produzione", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 3)


        self.label1 = QLabel("Temperatura", self)
        self.label2 = QLabel("Livello", self)
        self.label3 = QLabel("Composto", self)
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setAlignment(QtCore.Qt.AlignCenter)

        self.dato1 = QLabel("dato1", self)
        self.dato2 = QLabel("dato2", self)
        self.dato3 = QLabel("dato3", self)
        self.dato1.setStyleSheet("border: 1px solid black;")
        self.dato2.setStyleSheet("border: 1px solid black;")
        self.dato3.setStyleSheet("border: 1px solid black;")
        self.dato1.setAlignment(QtCore.Qt.AlignCenter)
        self.dato2.setAlignment(QtCore.Qt.AlignCenter)
        self.dato3.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.addWidget(self.label1, 1, 0, 1, 1)
        self.layout.addWidget(self.label2, 1, 1, 1, 1)
        self.layout.addWidget(self.label3, 1, 2, 1, 1)
        self.layout.addWidget(self.dato1, 2, 0, 1, 1)
        self.layout.addWidget(self.dato2, 2, 1, 1, 1)
        self.layout.addWidget(self.dato3, 2, 2, 1, 1)

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

    #controlla se c'è una produzione in corso
    #visualizza temperatura, livello, composto
    #effettua controllo della produzione
