from collections.abc import Iterable
import time

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, \
    QSpacerItem, QMessageBox, QDialogButtonBox, QDialog
from PyQt5 import QtCore

from Attivita.Prenotazione import Prenotazione
from Viste.VistaNuovaPrenotazione import VistaNuovaPrenotazione


class VistaPrenotazione(QWidget):

    def __init__(self, cliente, prenotazione):
        super(VistaPrenotazione, self).__init__()
        self.cliente = cliente
        self.prenotazione = prenotazione
        self.setWindowTitle('Gestione Prenotazione')
        self.layoutVert = QVBoxLayout()

        self.updateUI()

        self.setLayout(self.layoutVert)

    def updateUI(self):
        self.qLabel = QLabel()
        self.qLabel.setText(self.checkTime() + " %s" %self.cliente.nome)
        self.layoutVert.addWidget(self.qLabel)

        if self.prenotazione is None:
            self.qLabelNone = QLabel()
            self.qLabelNone.setText('Nessuna prenotazione attiva al momento')
            self.layoutVert.addWidget(self.qLabelNone)
        else:
            self.qLabelTrovata = QLabel()
            self.qLabelTrovata.setText('E\' stata trovata una prenotazione')
            self.layoutVert.addWidget(self.qLabelTrovata)

            self.layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
            self.layoutVert.addWidget(QLabel(f"Codice: {self.prenotazione.codice}"))
            self.layoutVert.addWidget(QLabel(f"Data Prenotazione: {self.prenotazione.dataInserimento}"))
            self.layoutVert.addWidget(QLabel(f"Importo Totale: {self.prenotazione.importoTotale} €"))
            self.layoutVert.addWidget(QLabel(f"Quantità Totale: {self.prenotazione.quantitaTotale}"))
            self.layoutVert.addWidget(QLabel(f"Confermata: {self.prenotazione.confermata}"))

            self.layoutVert.addWidget(QLabel(f"Elenco Prodotti: "))
            if isinstance(self.prenotazione.prodotti, Iterable):
                for elem in self.prenotazione.prodotti:
                    self.layoutVert.addWidget(QLabel(f"  Tipologia: {elem.tipologia} - Quantità: {elem.quantita}"))
            else:
                self.layoutVert.addWidget(QLabel(
                    f"  Tipologia: {self.prenotazione.prodotti.tipologia} - Quantità: {self.prenotazione.prodotti.quantita}"))

            self.layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.layoutBottoni = QHBoxLayout()

        bottoneNuovo = QPushButton('Nuovo')
        bottoneNuovo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneNuovo.clicked.connect(self.nuovaPrenotazione)
        self.layoutBottoni.addWidget(bottoneNuovo)

        bottoneModifica = QPushButton('Modifica')
        bottoneModifica.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneModifica.clicked.connect(self.modificaPrenotazione)
        self.layoutBottoni.addWidget(bottoneModifica)

        bottoneElimina = QPushButton('Elimina')
        bottoneElimina.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneElimina.clicked.connect(self.eliminaPrenotazione)
        self.layoutBottoni.addWidget(bottoneElimina)

        if self.prenotazione is None:
            bottoneNuovo.show()
            bottoneModifica.hide()
            bottoneElimina.hide()
        else:
            bottoneNuovo.hide()
            bottoneModifica.show()
            bottoneElimina.show()

        self.layoutVert.addLayout(self.layoutBottoni)

    def nuovaPrenotazione(self):
        self.vistaNuovaPrenotazione = VistaNuovaPrenotazione(self.cliente, 0, callback=self.updateUI)
        self.vistaNuovaPrenotazione.show()
        self.close()

    def modificaPrenotazione(self):
        self.vistaModificaPrenotazione = VistaNuovaPrenotazione(self.cliente, self.prenotazione.codice, callback=self.updateUI)
        self.vistaModificaPrenotazione.show()
        self.close()

    def eliminaPrenotazione(self):
        dlg = CustomDialog(self)
        if dlg.exec():
            Prenotazione().rimuoviPrenotazione(self.prenotazione.codice)
            msgBox = QMessageBox()
            msgBox.setText('Prenotazione eliminata con successo')
            msgBox.exec()
            self.prenotazione = None
            self.updateUI()
            self.close()

    def checkTime(self):
        mytime = time.localtime()
        if mytime.tm_hour < 14:
            return 'Buongiorno'
        else:
            return 'Buonasera'


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Attenzione")
        self.setStyleSheet('background-color: rgba(255, 255, 255);')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setText('L\' eliminazione della prenotazione è irreversibile\nProcedere comunque?')
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
