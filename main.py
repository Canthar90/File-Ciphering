import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel
from PyQt6.QtCore import Qt, QMimeData, QTimer
from pathlib import Path


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Simple GUI Template")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        text = QLabel('Please input file directory that you want to encrypt or decrypt')
        text.setStyleSheet('margin-left: 20px')

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Just drag and drop directory")
        self.input_field.setAcceptDrops(True)
        self.input_field.setStyleSheet("margin: 20px")

        button_layout = QHBoxLayout()  # Create a QHBoxLayout for the buttons

        self.green_button = QPushButton("Green Button")
        self.green_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px; margin-left: 20px")

        self.purple_button = QPushButton("Purple Button")
        self.purple_button.setStyleSheet("background-color: #673AB7; color: white; border-radius: 10px; padding: 10px; margin-right: 20px")

        self.blue_button = QPushButton("View logs")
        self.blue_button.setStyleSheet("background-color: #51829B; color: white; border-radius: 10px; padding: 15px")


        button_layout.addWidget(self.green_button)  # Add the green button to the button layout
        button_layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Add a spacer item to push the buttons to the sides
        button_layout.addWidget(self.purple_button)  # Add the purple button to the button layout

        
        layout.addWidget(text)
        layout.addWidget(self.input_field)
        layout.addLayout(button_layout)  # Add the button layout to the main layout

        layout.addWidget(self.blue_button, alignment=Qt.AlignmentFlag.AlignCenter)

        central_widget.setLayout(layout)

        self.green_button.clicked.connect(self.on_green_button_clicked)
        self.purple_button.clicked.connect(self.on_purple_button_clicked)
        self.blue_button.clicked.connect(self.on_blue_button_clicked)


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


    def on_green_button_clicked(self):
        # Simple animation
        self.green_button.setStyleSheet("background-color: #8BC34A; color: white; border-radius: 10px; padding: 8px; margin-left: 20px; border: 2px solid black")
        QTimer.singleShot(200, self.restore_green_button_style)  

        print("Green button clicked!")

    def restore_green_button_style(self):
        # Restore orginal state
        self.green_button.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 10px; padding: 10px; margin-left: 20px")


    def on_purple_button_clicked(self):
        # Simple animation
        self.purple_button.setStyleSheet("background-color: #9575CD; color: white; border-radius: 10px; padding: 8px; margin-right: 20px; border: 2px solid black")
        QTimer.singleShot(200, self.restore_purple_button_style)

        print("Purple button clicked!")


    def restore_purple_button_style(self):
        # Restore orginal state
        self.purple_button.setStyleSheet("background-color: #673AB7; color: white; border-radius: 10px; padding: 10px; margin-right: 20px")


    def on_blue_button_clicked(self):
        #simple Animation
        self.blue_button.setStyleSheet("background-color: #9BB0C1; color: white; border-radius: 10px; padding: 13px; border: 2px solid black")
        QTimer.singleShot(200, self.restore_blue_button_style)

        print("Blue button clicked")


    def restore_blue_button_style(self):
        # Restore style
        self.blue_button.setStyleSheet("background-color: #51829B; color: white; border-radius: 10px; padding: 15px")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())