
from PySide6.QtWidgets import QApplication, QLabel, QStatusBar, QMenu, QMainWindow, QWidget, QVBoxLayout, QFrame

from PySide6.QtGui import QPixmap, QFont, QAction


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Mon application")


        self.barre_menu = self.menuBar()
        self.menu1 = QMenu("&Menu1")
        self.action_menu1 = QAction("Item Menu1")
        self.menu1.addAction(self.action_menu1)
        self.menu1.triggered.connect(self.afficher_message_menu1)
        self.menu2 = QMenu("&Menu2")
        self.action_menu2 = QAction("Item Menu2")
        self.menu2.addAction(self.action_menu2)
        self.action_menu2.triggered.connect(self.afficher_message_menu2)

        self.barre_menu.addMenu(self.menu1)
        self.barre_menu.addMenu(self.menu2)

        label = QLabel()
        pixmap = QPixmap('ex1.png')
        label.setPixmap(pixmap)
        label.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)


        widget_central = QWidget()
        dispo = QVBoxLayout()
        widget_central.setLayout(dispo)
        dispo.addWidget(label)



        texte_riche = QLabel("Ceci est un texte riche ")
        police = QFont()
        police.setBold(True)
        police.setPointSize(15)
        police.setItalic(True)
        texte_riche.setFont(police)
        dispo.addWidget(texte_riche)

        self.setCentralWidget(widget_central)

        self.barre_statut = QStatusBar(self)
        self.setStatusBar(self.barre_statut)
        self.barre_statut.showMessage("Message de la barre de statut", 10000)


    def afficher_message_menu1(self):
        self.barre_statut.setStatusTip("Menu 1")

    def afficher_message_menu2(self):
        self.barre_statut.setStatusTip("Menu 2")


app = QApplication()
window = FenetrePrincipale()
window.show()
app.exec()

