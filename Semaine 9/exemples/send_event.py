from PySide6.QtCore import QSize, QEvent, Property
from PySide6.QtGui import QMouseEvent, Qt, QKeyEvent
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class Fenetre(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bouton = QPushButton("Cliquer moi!")
        self.setCentralWidget(self.bouton)
        MonEvenement.registerEventType()

    def bouton_clicked(self):
        # on construit un événement
        evenement = MonEvenement()


    # La méthode d'entrée de tous les événements
    def event(self, event: QEvent) -> bool:
        # Gère notre événement spécial
        if event.type() == MonEvenement:
            evenement = MonEvenement(event)
            return True
        # retourne pour les autres événements
        return QMainWindow.event(self, event)



class MonEvenement(QEvent):
    def __init__(self, event: QEvent):
        super().__init__(event)
        self._mon_texte = ""

    @Property(str)
    def mon_texte(self):
        return self._mon_texte

    @mon_texte.setter
    def mon_texte(self, mon_texte: str):
        self._mon_texte = mon_texte


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()