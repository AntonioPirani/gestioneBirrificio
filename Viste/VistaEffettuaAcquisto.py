from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QComboBox, QSpinBox, QListWidget, \
    QListWidgetItem, QSizePolicy


class VistaEffettuaAcquisto(QWidget):

    def __init__(self, callback):
        super(VistaEffettuaAcquisto, self).__init__()
        self.callback = callback
        self.setWindowTitle('Effettua Acquisto')

        self.layoutV = QVBoxLayout()
        self.qLines = {}
        self.label = QLabel('Inserisci i dati:')

        self.mylist = QListWidget()

        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)

        row = MyCustomWidget()
        item.setSizeHint(row.minimumSizeHint())

        self.mylist.setItemWidget(item, row)
        self.layoutV.addWidget(self.mylist)

        self.bottoneAggiungi = QPushButton('+')
        self.bottoneAggiungi.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.bottoneAggiungi.clicked.connect(self.addLine)
        self.layoutV.addWidget(self.bottoneAggiungi)

        self.setLayout(self.layoutV)

    def addLine(self):
        item = QListWidgetItem(self.mylist)
        self.mylist.addItem(item)

        row = MyCustomWidget()
        item.setSizeHint(row.minimumSizeHint())
        self.mylist.setItemWidget(item, row)


class MyCustomWidget(QWidget):
    def __init__(self, parent=None):
        super(MyCustomWidget, self).__init__(parent)

        self.row = QHBoxLayout()

        self.row.addWidget(QLabel('Tipologia'))
        comboBox = QComboBox()
        comboBox.addItem('Giana')
        comboBox.addItem('Papola')
        comboBox.addItem('Gradina')
        comboBox.addItem('Mezzavalle')
        self.row.addWidget(comboBox)

        self.row.addWidget(QLabel('Quantità'))
        self.row.addWidget(QSpinBox())

        self.setLayout(self.row)