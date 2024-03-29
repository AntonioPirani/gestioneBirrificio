from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore

from Viste.VistaAreaProduzione import VistaAreaProduzione
from Viste.VistaGestisciAcquisto import VistaGestisciAcquisto
from Viste.VistaVisualizzaInventario import VistaVisualizzaInventario


class VistaAreaRiservata(QWidget):

    def __init__(self, parent=None):
        super(VistaAreaRiservata, self).__init__(parent)

        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.setStyleSheet('background-color: rgba(255, 0, 0);')
        self.label = QLabel("Area Riservata", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 3)
        self.layout.addWidget(self.getButton('Effettua\nAcquisto', self.effettuaAcquisto), 1, 0)
        self.layout.addWidget(self.getButton('Visualizza\nInventario', self.visualizzaInventario), 1, 1)
        self.layout.addWidget(self.getButton('Inizia\nProduzione', self.iniziaProduzione), 1, 2)

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

    def effettuaAcquisto(self):
        self.vistaGestisciAcquisto = VistaGestisciAcquisto()
        self.vistaGestisciAcquisto.show()

    def visualizzaInventario(self):
        self.vistaVisualizzaInventario = VistaVisualizzaInventario()
        self.vistaVisualizzaInventario.show()

    def iniziaProduzione(self):
        self.vistaAreaProduzione = VistaAreaProduzione()
        self.vistaAreaProduzione.show()

