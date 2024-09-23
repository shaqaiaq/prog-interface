import csv

from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog

class FenetrePrincipale(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        self.prev_button = QPushButton("Precedent", self)
        self.next_button = None
        self.initUI()
        self.data = []
        self.current_index = -1

    def initUI(self):
        self.setWindowTitle("CSV Viewer")
        self.label = QLabel("No data loaded", self)

        self.prev_button.clicked.connect(self.show_prev_line)
        self.prev_button.setEnabled(False)

        self.next_button = QPushButton("Suivant", self)
        self.next_button.clicked.connect(self.show_next_line)
        self.next_button.setEnabled(False)


        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.prev_button)
        layout.addWidget(self.next_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        openFile = QAction("Ouvrir", self)
        openFile.triggered.connect(self.open_file)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu("Fichier")
        fileMenu.addAction(openFile)


    def open_file(self):
        options = QFileDialog.options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
        if fileName:
            self.load_data(fileName)

    def load_data(self, file_path):
        with open(file_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            self.data = list(reader)
        self.current_index = 0
        self.update_ui()


    def show_prev_line(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.update_ui()


    def show_next_line(self):
        if self.current_index < len(self.data) - 1:
            self.current_index += 1
            self.update_ui()


    def update_ui(self):
        if self.data:
            self.label.setText(",".join(self.data[self.current_index]))
            self.prev_button.setEnabled(self.current_index > 0)
            self.next_button.setEnabled(self.current_index < len(self.data) - 1)
        else:
            self.label.setText("No data loaded")
            self.prev_button.setEnabled(False)
            self.next_button.setEnabled(False)

app = QApplication()
viewer = FenetrePrincipale()
viewer.show()
app.exec()