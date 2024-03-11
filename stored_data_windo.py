from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6.QtCore import Qt


class StoredDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stored Clues")
        self.setGeometry(100, 100, 600, 200)

        centarl_widget = QWidget()
        self.setCentralWidget(centarl_widget)

        layout = QVBoxLayout()
        
        text = QLabel("This second window will contain clues saved in logs.json")

        layout.addWidget(text)

        centarl_widget.setLayout(layout)

        