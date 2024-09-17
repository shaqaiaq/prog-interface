from PySide6.QtWidgets import QApplication, QFrame, QLabel, QMainWindow, QWidget, QHBoxLayout
from PySide6.QtCore import QSize


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        cadre = QFrame()
        cadre.setFrameStyle(QFrame.Shape.Box | QFrame.Shadow.Raised)
        cadre.setBaseSize(QSize(250, 250))

        widget_central = QWidget()
        disposition = QHBoxLayout()
        widget_central.setLayout(disposition)
        disposition.addWidget(cadre)

        etiquette = QLabel("Etiquette")
        etiquette.setFrameStyle(QFrame.Shape.Panel | QFrame.Shadow.Sunken)
        disposition.addWidget(etiquette)

        self.setCentralWidget(widget_central)


app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()