from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore
from Viste.VistaClienti import VistaClienti

from Viste.VistaPrenotazione import VistaPrenotazione


class VistaAreaCliente(QWidget):

    def __init__(self, parent=None):
        super(VistaAreaCliente, self).__init__(parent)

        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.label = QLabel("Area Cliente", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.getButton('Registrazione', self.registrazione), 1, 0)
        self.layout.addWidget(self.getButton('Gestione\nPrenotazione', self.gestionePrenotazione), 1, 1)

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

    def registrazione(self):
        self.vistaRegistrazione = VistaClienti()
        self.vistaRegistrazione.show()

    def gestionePrenotazione(self):
        self.vistaPrenotazione = VistaPrenotazione()
        self.vistaPrenotazione.show()
        self.close()
