from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QProgressBar, QPushButton


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        widget_central = QWidget()
        disposition = QVBoxLayout()
        widget_central.setLayout(disposition)
        self.setCentralWidget(widget_central)

        self.barre_simple = QProgressBar()
        disposition.addWidget(self.barre_simple)

        self.barre_occupee = QProgressBar()
        self.barre_occupee.setMinimum(0)
        self.barre_occupee.setMaximum(0)
        disposition.addWidget(self.barre_occupee)

        bouton_avance = QPushButton("Avancer")
        disposition.addWidget(bouton_avance)
        self.avancement = 0
        bouton_avance.clicked.connect(self.bouton_avance)

    def bouton_avance(self):
        self.avancement = self.avancement + 10
        if self.avancement > 100:
            self.avancement = 100
        self.barre_simple.setValue(self.avancement)
        self.barre_occupee.setValue(self.avancement)

app = QApplication()
fp = FenetrePrincipale()
fp.show()
app.exec()
