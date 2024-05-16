import json
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QMessageBox

# Create a custom widget
class CustomMessageBox(QMessageBox):
    def __init__(self, json_data):
        super().__init__()

        self.json_data = json_data

        self.setWindowTitle("JSON Data")
        self.setIcon(QMessageBox.Icon.Information)
        self.setStandardButtons(QMessageBox.StandardButton.Ok)

        # Create a layout for the widget
        layout = QGridLayout()

        # Create a label to display the JSON data
        self.label = QLabel(self)
        self.label.setText(json.dumps(self.json_data))

        # Create a button to copy the JSON data to the clipboard
        self.copy_button = QPushButton(self)
        self.copy_button.setText("Copy")
        self.copy_button.clicked.connect(self.copy_data)

        # Add the label and button to the layout
        layout.addWidget(self.label, 0, 0)
        layout.addWidget(self.copy_button, 1, 0)

        # Set the layout for the widget
        self.setLayout(layout)

    def copy_data(self):
        # Get the text from the label
        text = self.label.text()

        # Copy the text to the clipboard
        clipboard = QClipboard()
        clipboard.setText(text)

# Create an instance of the custom widget
with open("logs.json", 'r') as f:
    json_data = json.load(f)
msg_box = CustomMessageBox(json_data)

# Show the message box
msg_box.show()
msg_box.exec()