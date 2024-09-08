import sys

from PySide6.QtGui import QAction, QIcon, QMovie
from PySide6.QtWidgets import QMainWindow, QApplication, QToolBar, QWidget, \
    QVBoxLayout, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle(" Lecteur de GIFs ")

        self.label = QLabel()
        self.movie = QMovie("sup.gif")
        self.label.setMovie(self.movie)
        self.movie.start()

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)


        self.action_jouer = QAction(QIcon("jouer.png"), "jouer",self)
        self.action_jouer.triggered.connect(self.jouer())
        self.action_stop = QAction(QIcon("stop.png"), "stop",self)
        self.action_stop.triggered.connect(self.stop())

        menu = self.menuBar().addMenu("Control bar")
        menu.addAction(self.action_jouer)
        menu.addAction(self.action_stop)

        toolbar = QToolBar("Control bar")
        toolbar.addAction(self.action_jouer)
        toolbar.addAction(self.action_stop)
        self.addToolBar(toolbar)


    def jouer(self):
        self.movie.start()

    def stop(self):
        self.movie.stop()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()