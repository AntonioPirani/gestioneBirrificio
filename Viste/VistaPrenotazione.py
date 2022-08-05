from collections.abc import Iterable

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QHBoxLayout, \
    QSpacerItem
from PyQt5 import QtCore


class VistaPrenotazione(QWidget):

    def __init__(self, cliente, prenotazione):
        super(VistaPrenotazione, self).__init__()
        self.cliente = cliente
        self.prenotazione = prenotazione
        self.setWindowTitle('Gestione Prenotazione')
        self.layoutVert = QVBoxLayout()

        self.qLabel = QLabel()
        self.qLabel.setText("Benvenuto %s" %cliente.nome)
        self.layoutVert.addWidget(self.qLabel)

        self.updateUI()

        self.setLayout(self.layoutVert)

    def onClick(self):
        print('Test')

    def updateUI(self):
        if self.prenotazione is None:
            self.qLabelNone = QLabel()
            self.qLabelNone.setText('Nessuna prenotazione attiva al momento')
            self.layoutVert.addWidget(self.qLabelNone)
        else:
            self.qLabelTrovata = QLabel()
            self.qLabelTrovata.setText('E\' stata trovata una prenotazione')
            self.layoutVert.addWidget(self.qLabelTrovata)

            self.layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
            self.layoutVert.addWidget(QLabel(f"Data Prenotazione: {self.prenotazione.dataInserimento}"))
            self.layoutVert.addWidget(QLabel(f"Importo Totale: {self.prenotazione.importoTotale} €"))
            self.layoutVert.addWidget(QLabel(f"Quantità Totale: {self.prenotazione.quantitaTotale}"))
            self.layoutVert.addWidget(QLabel(f"Confermata: {self.prenotazione.confermata}"))

            self.layoutVert.addWidget(QLabel(f"Elenco Prodotti: "))
            if isinstance(self.prenotazione.prodotti, Iterable):
                for elem in self.prenotazione.prodotti:
                    self.layoutVert.addWidget(QLabel(f"  Tipologia: {elem.tipologia} - Quantità: {elem.quantita}"))
                    # layoutVert.addWidget(QLabel(f"Quantità: {elem.quantita}"))
            else:
                self.layoutVert.addWidget(QLabel(
                    f"  Tipologia: {self.prenotazione.prodotti.tipologia} - Quantità: {self.prenotazione.prodotti.quantita}"))

            # layoutVert.addWidget(QLabel(f""))

            self.layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        self.layoutBottoni = QHBoxLayout()

        bottoneNuovo = QPushButton('Nuovo')
        bottoneNuovo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneNuovo.clicked.connect(self.onClick)
        self.layoutBottoni.addWidget(bottoneNuovo)

        bottoneModifica = QPushButton('Modifica')
        bottoneModifica.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneModifica.clicked.connect(self.onClick)
        self.layoutBottoni.addWidget(bottoneModifica)

        bottoneElimina = QPushButton('Elimina')
        bottoneElimina.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneElimina.clicked.connect(self.onClick)
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




