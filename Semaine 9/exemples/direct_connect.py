from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QWidget


class Fenetre(QMainWindow):

    def __init__(self):
        super().__init__()
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        disposition = QVBoxLayout()
        etiquette = QLabel("")
        edit = QLineEdit()

        # le signal textChanged du QLine Edit émet une str contenant le nouveau texte. En le connectant à la
        # fente (slot) setText du QLabel, le setText du QLabel sera appelé avec la str contenant le nouveau texte en
        # paramètre.
        edit.textChanged.connect(etiquette.setText)

        disposition.addWidget(etiquette)
        disposition.addWidget(edit)
        widget_central.setLayout(disposition)


app = QApplication()
fenetre = Fenetre()
fenetre.show()
app.exec()