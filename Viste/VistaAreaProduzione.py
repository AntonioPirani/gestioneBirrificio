from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore

class VistaAreaProduzione(QWidget):

    def __init__(self, parent=None):
        super(VistaAreaProduzione, self).__init__(parent)

        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.label = QLabel("Area Produzione", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.getButton('Inserisci\nmaterie\nprime', self.materieUtilizzate), 1, 0)
        self.layout.addWidget(self.getButton('Visualizza\ndati', self.dati), 1, 1)

        self.resize(400, 300)
        self.setWindowTitle("Gestore Birrificio")
        self.setLayout(self.layout)
        self.show()

    def getButton(self, titolo, on_click):
        button = QPushButton(titolo)
        button.setStyleSheet('background-color: rgba(255, 153, 0);'
                             'font: 87 14pt "Arial";color: rgb(255, 255, 127);')
        button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def materieUtilizzate(self):
        print('Insersci le materei che vuoi impiegare')

    def dati(self):
        print('Visualizza dati della produzione')

    #controlla se ce una produzione attiva
    #scegli le materie prime da inserire, la quantita
    #stampa dati