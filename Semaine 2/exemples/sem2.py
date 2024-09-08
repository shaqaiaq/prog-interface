import sys

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QStatusBar, QPushButton, QDialog, QWidget, \
    QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(" Mon application ")

# Barre de statut
        self.statusBar = QStatusBar()
        self.statusBar.setStatusTip("Click!")
        self.setStatusBar(self.statusBar)
# Menu
        barre_menus = self.menuBar()
        self.creer_menus(barre_menus)
# Barre d'outils
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)

        toolbar_bouton = QPushButton("Toolbar Button")
        toolbar_bouton.clicked.connect(lambda: print("Toolbar button clicked"))
        toolbar.addWidget(toolbar_bouton)

        central_wedget = QWidget()
        layout = QVBoxLayout()
        central_wedget.setLayout(layout)

        central_button = QPushButton("Open Dialog")
        central_button.clicked.connect(self.open_dialog)
        layout.addWidget(central_button)

        self.setCentralWidget(central_wedget)

    def creer_menus(self, barre_menus):
        menu_1 = barre_menus.addMenu("&Menu1")
        action1 = QAction("Action1", self)
        action1.setStatusTip("Check!")
        menu_1.addAction(action1)

        menu_2 = barre_menus.addMenu("M&enu2")
        action2 = QAction("Action2 ", self)
        action2.setStatusTip("Hello!")
        menu_2.addAction(action2)

    def open_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog")
        dialog_layout = QVBoxLayout()
        dialog.setLayout(dialog_layout)

        close_button = QPushButton("Close Dialog")
        close_button.clicked.connect(dialog.accept)
        dialog_layout.addWidget(close_button)

        dialog.exec()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()

