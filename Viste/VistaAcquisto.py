from collections.abc import Iterable

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout

from Attivita.Acquisto import Acquisto


class VistaAcquisto(QWidget):

    def __init__(self, acquisto, eliminaCallback):
        super(VistaAcquisto, self).__init__()
        self.setWindowTitle('Acquisto')
        self.eliminaCallback = eliminaCallback
        layoutVert = QVBoxLayout()

        nome = ''
        info = {}

        if isinstance(acquisto, Acquisto):
            nome = f"Acquisto {acquisto.codice}"
            info = acquisto.getInfoAcquisto()
        labelNome = QLabel(nome)
        labelNome.setFont(QFont('Arial', 10))
        layoutVert.addWidget(labelNome)

        layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        layoutVert.addWidget(QLabel(f"Data Acquisto: {info['dataAcquisto']}"))
        layoutVert.addWidget(QLabel(f"Importo Totale: {info['importoTotale']} €"))
        layoutVert.addWidget(QLabel(f"Quantità Totale: {info['quantitaTotale']}"))

        layoutVert.addWidget(QLabel(f"Elenco Prodotti: "))
        if isinstance(info['elencoProdotti'], Iterable):
            for elem in info['elencoProdotti']:
                layoutVert.addWidget(QLabel(f"  Tipologia: {elem.tipologia} - Quantità: {elem.quantita}"))
                #layoutVert.addWidget(QLabel(f"Quantità: {elem.quantita}"))
        else:
            layoutVert.addWidget(QLabel(f"  Tipologia: {info['elencoProdotti'].tipologia} - Quantità: {info['elencoProdotti'].quantita}"))

        #layoutVert.addWidget(QLabel(f""))

        layoutVert.addItem(QSpacerItem(10, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))
        self.setLayout(layoutVert)