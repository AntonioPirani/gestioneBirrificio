from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox, QHBoxLayout
from PyQt5 import QtCore

from Attivita.Cliente import Cliente
from Attivita.Prenotazione import Prenotazione
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
        dlg = CustomLogin(self)
        if dlg.exec():
            if dlg.qLineLog.text() != "" and dlg.qLinePW.text() != "":
                #autentica utente:
                cliente = Cliente().autenticaCliente(dlg.qLineLog.text(), dlg.qLinePW.text())
                if cliente is not False:
                    #cliente autenticato
                    prenotazione = Prenotazione().ricercaPrenotazioneCliente(cliente.codiceFiscale)
                    self.vistaPrenotazione = VistaPrenotazione(cliente, prenotazione)
                    self.vistaPrenotazione.show()

                else:
                    QMessageBox.critical(self, 'Errore', 'Cliente non autenticato', QMessageBox.Ok, QMessageBox.Ok)
        else:
            pass


class CustomLogin(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet('background-color: rgba(255, 255, 255);')
        self.setWindowTitle("Accedi")

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layoutGrid = QGridLayout()

        self.qLabel = QLabel()
        self.qLabel.setText("Codice: ")
        self.layoutGrid.addWidget(self.qLabel, 0, 0)
        self.qLineLog = QLineEdit()
        self.layoutGrid.addWidget(self.qLineLog, 0, 1)

        self.qLabelPw = QLabel()
        self.qLabelPw.setText("Password:")
        self.layoutGrid.addWidget(self.qLabelPw, 1, 0)
        self.qLinePW = QLineEdit()
        self.qLinePW.setEchoMode(QLineEdit.Password)
        self.layoutGrid.addWidget(self.qLinePW, 1, 1)

        self.layout.addLayout(self.layoutGrid)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

