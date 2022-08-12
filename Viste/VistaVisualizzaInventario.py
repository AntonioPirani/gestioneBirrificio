import os
import pickle

from PyQt5.QtGui import QStandardItemModel, QStandardItem, QFont
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QListView
from Viste.VistaAggiungiMateria import VistaAggiungiMateria

class VistaVisualizzaInventario(QWidget):

    def __init__(self):
        super(VistaVisualizzaInventario, self).__init__()
        self.setWindowTitle('Inventario')
        layoutOriz = QHBoxLayout()
        layoutVert = QVBoxLayout()
        self.listView_materia = QListView()
        self.listView_prodotto = QListView()
        self.visualizzaInventario()
        layoutOriz.addWidget(self.listView_materia)
        layoutOriz.addWidget(self.listView_prodotto)
        layoutVert.addLayout(layoutOriz)
        layoutBottone = QHBoxLayout()
        bottoneInserisci = QPushButton(' Inserisci Materia')
        bottoneInserisci.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        bottoneInserisci.clicked.connect(self.nuovaMateria)
        layoutBottone.addWidget(bottoneInserisci)
        layoutVert.addLayout(layoutBottone)
        self.setLayout(layoutVert)
        self.resize(600, 300)

    def nuovaMateria(self):
        self.aggiungiMateria = VistaAggiungiMateria(callback=self.visualizzaInventario)
        self.aggiungiMateria.show()

    def caricaInventario(self):
        if os.path.isfile('Dati\Inventario.pickle'):
            with open('Dati\Inventario.pickle', 'rb') as f:
                app = dict(pickle.load(f))
                self.inventario.extend(app.values())

    def visualizzaInventario(self):
        self.inventario = []
        self.caricaInventario()
        listViewModelMaterie = QStandardItemModel(self.listView_materia)
        listViewModelProdotto = QStandardItemModel(self.listView_prodotto)
        for mat in self.inventario:
            item = QStandardItem()
            if type(mat).__name__ == "Bottiglia":
                nome = f"{type(mat).__name__} Tipo: {mat.tipologia} Quantita: {mat.quantita}"
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Arial', 10))
                listViewModelProdotto.appendRow(item)
            else:
                nome = f"{type(mat).__name__} Nome: {mat.nome} Quantita: {mat.quantita}"
                item.setText(nome)
                item.setEditable(False)
                item.setFont(QFont('Arial', 10))
                listViewModelMaterie.appendRow(item)

        self.listView_materia.setModel(listViewModelMaterie)
        self.listView_prodotto.setModel(listViewModelProdotto)

    
