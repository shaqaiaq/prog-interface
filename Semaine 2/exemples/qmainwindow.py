import sys

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QLabel, QStatusBar, QPushButton
from PySide6.QtGui import QAction, QKeySequence, QIcon


class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super(FenetrePrincipale, self).__init__()

        label_texte = QLabel("texteasdfsadfsadfdsaf")

        self.setCentralWidget(label_texte)

        barre_menus = self.menuBar()
        self.creer_menus(barre_menus)

        icone = QIcon("jouer.png")

        bouton_test = QPushButton("Test")
        bouton_test.setIcon(icone)
        bouton_test.pressed.connect(self.action_executee)



        barre_outils = QToolBar("Barre d'outils")
        barre_outils.setIconSize(QSize(16, 16))
        barre_outils.addWidget(bouton_test)
        self.addToolBar(barre_outils)

        barre_outils_2 = QToolBar("Barre d'outils 2")
        barre_outils_2.setIconSize(QSize(16, 16))
        bouton_outils = QPushButton("Outils")
        bouton_outils.pressed.connect(self.action_executee)
        barre_outils_2.addWidget(bouton_outils)
        self.addToolBar(barre_outils_2)

        self.barre_statut = QStatusBar(self)
        self.barre_statut.setStatusTip("cliquer un bouton")
        self.setStatusBar(self.barre_statut)

    def creer_menus(self, barre_menus):
        menu_fichier = barre_menus.addMenu("&Fichier")
        action_test = QAction(text="Test!", parent=self)
        action_test.setStatusTip("Cliquez pour un test")
        action_test.triggered.connect(self.action_executee)
        menu_fichier.addAction(action_test)

        menu_quitter = barre_menus.addMenu("&Quitter")
        action_quitter = QAction(text="Quitter", parent=self)
        action_quitter.triggered.connect(self.close)
        action_quitter.setShortcut(QKeySequence("Ctrl+Q"))
        menu_quitter.addAction(action_quitter)

    def action_executee(self):
        print("click!!!")
        self.barre_statut.setStatusTip("click!!!!!!!")


app = QApplication(sys.argv)
f = FenetrePrincipale()
f.show()
app.exec()