from PySide6.QtCore import QSize
from PySide6.QtGui import QMouseEvent, Qt, QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel


class Fenetre(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setFixedSize(QSize(200, 200))
        self.compteur = 0
        self.etiquette = QLabel(str(self.compteur))
        self.setCentralWidget(self.etiquette)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        # On va changer le QLabel sur un click droit
        if event.button() == Qt.MouseButton.RightButton:
            self.compteur += 1
            self.etiquette.setText(str(self.compteur))
        else:
            # On appelle la méthode parente pour gérer les autres boutons normalement
            QMainWindow.mousePressEvent(self, event)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()
