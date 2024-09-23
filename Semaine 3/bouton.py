from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QVBoxLayout


class FenetrePrincipale(QMainWindow):

    def __init__(self):
        super().__init__()

        self.label = QLabel("L'informatique, ça fait gagner beaucoup de temps... à condition d'en avoir beaucoup devant soi!")


        self.bouton_italique = QPushButton("Italique")
        self.bouton_italique.setCheckable(True)
        self.bouton_italique.clicked.connect(self.bouton_italique_clicked)
        self.bouton_gras = QPushButton("Caractères gras")
        self.bouton_gras.setCheckable(True)
        self.bouton_gras.clicked.connect(self.bouton_gras_clicked)
        self.bouton_wordwrap = QPushButton("wordWrap")
        self.bouton_wordwrap.setCheckable(True)
        self.bouton_wordwrap.clicked.connect(self.bouton_wordwrap_clicked)
        self.bouton_aug_police = QPushButton("Augmenter taille")
        self.bouton_aug_police.setCheckable(True)
        self.bouton_aug_police.clicked.connect(self.bouton_aug_police_clicked)
        self.bouton_dim_police = QPushButton("Diminuer taille")
        self.bouton_dim_police.setCheckable(True)
        self.bouton_dim_police.clicked.connect(self.bouton_dim_police_clicked)
        self.bouton_tous = QPushButton("Désactiver/Activer tous bouton")
        self.bouton_tous.setCheckable(True)
        self.bouton_tous.clicked.connect(self.bouton_tous_clicked)

        widget_central = QWidget()
        dispo = QVBoxLayout()
        widget_central.setLayout(dispo)
        dispo.addWidget(self.label)
        dispo.addWidget(self.bouton_italique)
        dispo.addWidget(self.bouton_gras)
        dispo.addWidget(self.bouton_wordwrap)
        dispo.addWidget(self.bouton_aug_police)
        dispo.addWidget(self.bouton_dim_police)
        dispo.addWidget(self.bouton_tous)

        self.setCentralWidget(widget_central)




    def bouton_italique_clicked(self):
        font = self.label.font()
        font.setItalic(self.bouton_italique.isChecked())
        self.label.setFont(font)


    def bouton_gras_clicked(self):
        font = self.label.font()
        font.setBold(self.bouton_gras.isChecked())
        self.label.setFont(font)

    def bouton_wordwrap_clicked(self):
        self.label.setWordWrap(self.bouton_wordwrap.isChecked())

    def bouton_aug_police_clicked(self):
        font = self.label.font()
        font.setPointSize(font.pointSize() + 1)
        self.label.setFont(font)

    def bouton_dim_police_clicked(self):
        font = self.label.font()
        font.setPointSize(font.pointSize() - 1)
        self.label.setFont(font)

    def bouton_tous_clicked(self):
        state = not self.bouton_tous.isChecked()
        self.bouton_italique.setEnabled(state)
        self.bouton_gras.setEnabled(state)
        self.bouton_wordwrap.setEnabled(state)
        self.bouton_aug_police.setEnabled(state)
        self.bouton_dim_police.setEnabled(state)
        self.bouton_tous.setEnabled(state)




app = QApplication()
window = FenetrePrincipale()
window.show()
app.exec()