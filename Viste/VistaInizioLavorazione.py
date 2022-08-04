from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QComboBox, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox, QSpinBox
from PyQt5 import QtCore

class VistaInizioLavorazione(QWidget):

    def __init__(self, parent=None):
        super(VistaInizioLavorazione, self).__init__(parent)

        self.label = QLabel("Area Inizio Lavorazione", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 5)

        self.label1 = QLabel("Materia", self)
        self.label2 = QLabel("Quantità", self)

        self.lineedit1 = QComboBox(self)
        self.lineedit2 = QSpinBox(self)

        self.layout.addWidget(self.label1, 1, 0, 1, 1)
        self.layout.addWidget(self.label2, 1, 3, 1, 1)

        self.layout.addWidget(self.lineedit1, 1, 1, 1, 2)
        self.layout.addWidget(self.lineedit2, 1, 4, 1, 2)

        self.lineedit1.addItem("Vienna")
        self.lineedit1.addItem("Monaco")

        self.button = QPushButton("Inizia Lavorazione")

        self.layout.addWidget(self.button, 2, 4, 1, 1)

        self.resize(400, 350)
        self.setWindowTitle("Vista Inizio Lavorazione")
        self.setLayout(self.layout)
        self.show()