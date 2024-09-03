from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget, QVBoxLayout
import sys
import random
class FenetrePrincipale(QMainWindow):
    def handle_button_ok(self):
        print("Click!")
        label_equations = [
           "a^2 + b^2 = c^2",
           "ln(xy) = ln(x) + ln(y)",
           "i^2 = 1",
           "E = mc^2"

         ]
        equations = random.choice(label_equations)
        self.label.setText(equations)



    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Semaine1 ")
        self.label = QLabel("Cliquez pour une equation", self)
        self.button = QPushButton("Cliquez-moi", self)
        self.button.clicked.connect(self.handle_button_ok)
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.label)
        main_layout.addWidget(self.button)

        main_container = QWidget()
        main_container.setLayout(main_layout)

        self.setCentralWidget(main_container)


        # Affichage de la fenetre
        self.show()



# Creation de l'application
app = QApplication(sys.argv)
# Creation de la fenetre (la classe ci-haut)
w = FenetrePrincipale()
w.show()
# execution
sys.exit(app.exec())
