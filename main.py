import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QMimeData
from pathlib import Path


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple GUI Template")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Drag and drop folder or file here")
        self.input_field.setAcceptDrops(True)

        button_layout = QHBoxLayout()  # Create a QHBoxLayout for the buttons

        green_button = QPushButton("Green Button")
        green_button.setStyleSheet("background-color: green")

        purple_button = QPushButton("Purple Button")
        purple_button.setStyleSheet("background-color: purple")

        button_layout.addWidget(green_button)  # Add the green button to the button layout
        button_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Add a spacer item to push the buttons to the sides
        button_layout.addWidget(purple_button)  # Add the purple button to the button layout

        layout.addWidget(self.input_field)
        layout.addLayout(button_layout)  # Add the button layout to the main layout

        central_widget.setLayout(layout)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        if urls:
            path = Path(urls[0].toLocalFile())
            if path.is_dir():
                self.input_field.setText(str(path))
            elif path.is_file():
                self.input_field.setText(str(path))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())