import random
from copy import deepcopy

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QHBoxLayout, QListWidget, QLineEdit, QLabel, QSizePolicy, QPushButton, QListWidgetItem, \
    QMessageBox, QVBoxLayout, QComboBox, QSpinBox, QWidget

from Attivita.Prenotazione import Prenotazione
from Servizio.Bottiglia import Bottiglia


class VistaNuovaPrenotazione(QWidget):
    def __init__(self, cliente, codice, callback):
        super(VistaNuovaPrenotazione, self).__init__()
        self.callback = callback
        self.setFont(QFont('Arial', 10))
        self.setWindowTitle('Prenotazione')
        self.cliente = cliente
        self.codice = codice
        self.massimo = 0

        self.layoutV = QVBoxLayout()
        self.mylist = QListWidget()

        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)

        row = MyCustomWidget()
        item.setSizeHint(row.minimumSizeHint())

        self.mylist.setItemWidget(item, row)
        self.layoutV.addWidget(self.mylist)

        self.boxH = QHBoxLayout()

        self.bottoneAggiungi = QPushButton('+')
        self.bottoneAggiungi.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.bottoneAggiungi.clicked.connect(self.addLine)
        self.boxH.addWidget(self.bottoneAggiungi)

        self.bottoneConferma = QPushButton('Conferma')
        self.bottoneConferma.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.bottoneConferma.clicked.connect(self.confermaPrenotazione)
        self.boxH.addWidget(self.bottoneConferma)
        self.layoutV.addLayout(self.boxH)

        self.setLayout(self.layoutV)

    def addLine(self):
        self.massimo += 1
        if self.massimo >= 3:
            self.bottoneAggiungi.hide()
            pass

        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)

        row = MyCustomWidget()
        item.setSizeHint(row.minimumSizeHint())
        self.mylist.setItemWidget(item, row)

    def confermaPrenotazione(self):

        prenotazione = Prenotazione()
        elenco = []
        errore = False
        self.carrello = {}
        for i in range(self.mylist.count()):
            item = self.mylist.item(i)
            widget = self.mylist.itemWidget(item)
            if widget is not None:
                tipologia = widget.getTipologia()
                quantita = widget.getQuantita()
                if tipologia in self.carrello or quantita == 0:
                    errore = True
                    break

                bot = Bottiglia().aggiungiBottiglia(tipologia, quantita)
                d = deepcopy(bot)
                elenco.append(d)

                self.carrello[tipologia] = bot

        if errore:
            QMessageBox.critical(self, 'Errore', 'Inserisci i dati corretti', QMessageBox.Ok, QMessageBox.Ok)

        else:
            verifica = False
            if self.codice == 0:
                n = random.randint(1, 999999)
                verifica = prenotazione.aggiungiPrenotazione(n, self.cliente, elenco)
            else:
                n = self.codice
                verifica = prenotazione.modificaPrenotazione(n, self.cliente, elenco)

            if not verifica:
                QMessageBox.critical(self, 'Errore', 'Prenotazione non andata a buon fine', QMessageBox.Ok,
                                     QMessageBox.Ok)
            else:
                self.msgBox()

            self.callback()
            self.close()

    def msgBox(self):
        msg = QMessageBox()
        msg.setWindowTitle('Successo')
        msg.setText("Prenotazione effettuata con successo!")
        msg.setIcon(1)
        msg.exec()

class MyCustomWidget(QWidget):
    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.row.addWidget(QLabel('Tipologia'))
        self.comboBox = QComboBox()
        self.comboBox.addItem('Giana')
        self.comboBox.addItem('Papola')
        self.comboBox.addItem('Gradina')
        self.comboBox.addItem('Mezzavalle')
        self.row.addWidget(self.comboBox)

        self.row.addWidget(QLabel('Quantità'))
        self.spinBox = QSpinBox()
        self.row.addWidget(self.spinBox)

        self.setLayout(self.row)

    def getTipologia(self):
        return self.comboBox.currentText()

    def getQuantita(self):
        return self.spinBox.value()
