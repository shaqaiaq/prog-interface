from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        self.bouton_texte = QPushButton("Ornithorynque")
        self.bouton_texte.clicked.connect(self.bouton_texte_clicked)
        self.bouton_icone = QPushButton()
        self.bouton_icone.setIcon(QIcon('platypus.png'))
        self.bouton_icone.clicked.connect(self.bouton_icone_clicked)
        self.bouton_mixte = QPushButton(QIcon('platypus.png'), "Ornithorynque")

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        disposition.addWidget(self.bouton_texte)
        disposition.addWidget(self.bouton_icone)
        disposition.addWidget(self.bouton_mixte)

        self.setCentralWidget(widget_central)

    def bouton_texte_clicked(self):
        self.bouton_texte.setEnabled(False)

    def bouton_icone_clicked(self):
        grandeur = self.bouton_icone.size()
        grandeur.setWidth(self.bouton_icone.size().width()+10)
        self.bouton_icone.setIconSize(grandeur)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()
