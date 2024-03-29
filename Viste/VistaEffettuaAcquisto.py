import random
import sys
from copy import deepcopy

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox, QSpinBox, QListWidget, \
    QListWidgetItem, QSizePolicy, QMessageBox, QLineEdit

from Attivita.Acquisto import Acquisto
from Servizio.Bottiglia import Bottiglia


class VistaEffettuaAcquisto(QWidget):

    def __init__(self, callback):
        super(VistaEffettuaAcquisto, self).__init__()
        self.callback = callback
        self.setFont(QFont('Arial', 10))
        self.setWindowTitle('Effettua Acquisto')
        self.massimo = 0

        self.boxPrenotazione = QHBoxLayout()
        self.labelPrenotazione = QLabel()
        self.labelPrenotazione.setText('Codice Prenotazione:')
        self.inserimentoPrenotazione = QLineEdit()
        self.inserimentoPrenotazione.setToolTip('Valori ammessi: 0-9')
        self.inserimentoPrenotazione.setInputMask('999999')
        self.boxPrenotazione.addWidget(self.labelPrenotazione)
        self.boxPrenotazione.addWidget(self.inserimentoPrenotazione)

        self.layoutV = QVBoxLayout()
        self.layoutV.addLayout(self.boxPrenotazione)
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
        self.bottoneConferma.clicked.connect(self.confermaAcquisto)
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

    def confermaAcquisto(self):

        acquisto = Acquisto()
        if self.inserimentoPrenotazione.text() != '' and self.inserimentoPrenotazione.text() != '0':
            self.codicePrenotazione = int(self.inserimentoPrenotazione.text())  #set no edit?
            verifica = acquisto.effettuaAcquisto(0, None, self.codicePrenotazione)
            if not verifica:
                QMessageBox.critical(self, 'Errore', 'Prenotazione non valida', QMessageBox.Ok, QMessageBox.Ok)
            else:
                self.msgBox(acquisto.importoTotale)

        else:

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
                #print(self.carrello.values()) # da provare
                #print(elenco)   # prima scelta

                n = random.randint(1, 999999)  #sys.maxsize
                verifica = acquisto.effettuaAcquisto(n, elenco) #acquisto.effettuaAcquisto(1, self.carrello.values())
                if not verifica:
                    QMessageBox.critical(self, 'Errore', 'Acquisto non andato a buon fine', QMessageBox.Ok, QMessageBox.Ok)
                else:
                    self.msgBox(acquisto.importoTotale)

        self.callback()
        self.close()

    def msgBox(self, importo):
        msg = QMessageBox()
        msg.setWindowTitle('Successo')
        msg.setText("Importo da pagare: %s €" %importo)
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