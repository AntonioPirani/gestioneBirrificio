import datetime
from copy import deepcopy

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel, QListWidget, \
    QListWidgetItem, QComboBox, QSpinBox, QMessageBox

from Attivita.Inventario import Inventario
from Attivita.Materia import Materia


class VistaAggiungiMateria(QWidget):

    def __init__(self, callback):
        super(VistaAggiungiMateria, self).__init__()

        self.callback = callback
        self.setWindowTitle('Aggiungi Materia')

        self.layoutV = QVBoxLayout()
        self.qLines = {}
        self.label = QLabel('Inserisci i dati:')
        self.mylist = QListWidget()
        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)
        row = AggiungiMateriaWidget()
        item.setSizeHint(row.minimumSizeHint())
        self.mylist.setItemWidget(item, row)
        self.layoutV.addWidget(self.mylist)

        self.boxH = QHBoxLayout()

        self.bottoneAggiungi = QPushButton('+')
        self.bottoneAggiungi.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.bottoneAggiungi.clicked.connect(self.aggiungiMateria)
        self.boxH.addWidget(self.bottoneAggiungi)

        self.bottoneConferma = QPushButton('Conferma')
        self.bottoneConferma.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.bottoneConferma.clicked.connect(self.confermaMateria)
        self.boxH.addWidget(self.bottoneConferma)

        self.layoutV.addLayout(self.boxH)
        self.setLayout(self.layoutV)

    def aggiungiMateria(self):
        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)

        row = AggiungiMateriaWidget()
        item.setSizeHint(row.minimumSizeHint())
        self.mylist.setItemWidget(item, row)

    def confermaMateria(self):
        inventario = Inventario()
        elenco = []
        errore = False
        self.carrello = {}
        for i in range(self.mylist.count()):
            item = self.mylist.item(i)
            widget = self.mylist.itemWidget(item)
            if widget is not None:
                nome = widget.getNome()
                quantita = widget.getQuantita()

                if nome in self.carrello or quantita == 0:
                    errore = True
                    break

                mat = Materia().aggiungiMateria(1, "", "", nome, quantita, datetime.datetime(1970, 1, 1, 0, 0))
                d = deepcopy(mat)
                elenco.append(d)
                #print(type(elenco).__name__) #list
                #print(type(mat).__name__)   #Materia
                print("\nbreak\n")
                self.carrello[nome] = mat

        if errore:
            QMessageBox.critical(self, 'Errore', 'Inserisci i dati corretti', QMessageBox.Ok, QMessageBox.Ok)
        else:
            for materia in elenco:
                inventario.aggiornaMagazzino(materia)
            
        self.callback()
        self.close()


class AggiungiMateriaWidget(QWidget):
    def __init__(self, parent=None):
        super(AggiungiMateriaWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.row.addWidget(QLabel('Nome'))
        self.comboBox = QComboBox()
        self.comboBox.addItem('Monaco')
        self.comboBox.addItem('Vienna')
        self.comboBox2.addItem("Pilsen ")
        self.comboBox2.addItem("Carapilsen")
        self.row.addWidget(self.comboBox)

        self.row.addWidget(QLabel('Quantità'))
        self.spinBox = QSpinBox()
        self.row.addWidget(self.spinBox)

        self.setLayout(self.row)

    def getNome(self):
        return self.comboBox.currentText()

    def getQuantita(self):
        return self.spinBox.value()
