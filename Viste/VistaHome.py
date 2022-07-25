from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy, QLabel, QVBoxLayout, QDialogButtonBox, \
    QDialog, QLineEdit, QMessageBox
from PyQt5 import QtCore


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome, self).__init__(parent)

        self.setStyleSheet('background-color: rgba(255, 0, 0);')
            #TODO provare cosi lo stile
        self.label = QLabel("Gestione Birrificio", self)
        self.label.setStyleSheet('font: 87 20pt "Arial Black";color: rgb(255, 255, 127);'
                                 'background-color: rgba(255, 153, 0);')
        self.label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        self.layout = QGridLayout()
        self.layout.addWidget(self.label, 0, 0, 1, 2)
        self.layout.addWidget(self.getButton('Area Riservata', self.selezionaAreaRiservata), 1, 0)
        self.layout.addWidget(self.getButton('Area Clienti', self.selezionaAreaCliente), 1, 1)

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

    def selezionaAreaRiservata(self):
        dlg = CustomDialog(self)
        if dlg.exec() and dlg.qLine.text() == 'birra':
            # self.vistaAreaRiservata = VistaAreaRiservata()
            # self.vistaAreaRiservata.show()
            print(dlg.qLine.text())
        else:
            msgBox = QMessageBox()
            msgBox.setText('Errore inserimento password')
            msgBox.exec();
        pass

    def selezionaAreaCliente(self):
        print('Benvenuto!')


class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Conferma")
        self.setStyleSheet('background-color: rgba(255, 255, 255);')

        QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.qLine = QLineEdit()
        self.qLine.setEchoMode(QLineEdit.Password)
        self.layout.addWidget(self.qLine)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
