import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel, QMessageBox, QTextBrowser, QTextEdit, QTableWidget, QTableWidgetItem
from PyQt6.QtCore import Qt, QMimeData, QTimer, QVariant, QJsonDocument
from pathlib import Path

import json

from file_cyphering import EncryptFiles


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DirCypher")
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

        self.green_button = QPushButton("Cipher file")
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
        if self.input_field.text() != '':
            
            enctyptor = EncryptFiles()
            enctyptor.encrypt_data_selected(self.input_field.text())
            self.json_data_popup()
        
        QTimer.singleShot(200, self.restore_green_button_style)  



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

        self.json_data_popup()

    def json_data_popup(self):
        with open('logs.json', 'r') as f:
            data = json.load(f)
        

        text_browser = QTableWidget()
        text_browser.setColumnCount(len(data[0][0]))
        text_browser.setRowCount(len(data))
        text_browser.setMinimumWidth(300)
        for i, row in enumerate(data):
            for x, row_2 in enumerate(row):
                for j, (key, val)in enumerate(row_2.items()):
                    item = QTableWidgetItem(str(val))
                    text_browser.setItem(i, j, item)
            

        msg = QMessageBox()
        msg.layout().addWidget(text_browser)
        msg.setText("Click Show Details to see your logs")
        
        msg.exec()



    def restore_blue_button_style(self):
        # Restore style
        self.blue_button.setStyleSheet("background-color: #51829B; color: white; border-radius: 10px; padding: 15px")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())









# class CustomMessageBox(QMessageBox):
#     def __init__(self, json_data):
#         super().__init__()

#         self.json_data = json_data

#         self.setWindowTitle("JSON Data")
#         self.setIcon(QMessageBox.Icon.Information)
#         self.setStandardButtons(QMessageBox.StandardButton.Ok)

#         # Create a layout for the widget
#         layout = QGridLayout()

#         # Create a label to display the JSON data
#         self.label = QLabel(self)
#         self.label.setText(json.dumps(self.json_data))

#         # Create a button to copy the JSON data to the clipboard
#         self.copy_button = QPushButton(self)
#         self.copy_button.setText("Copy")
#         self.copy_button.clicked.connect(self.copy_data)

#         # Add the label and button to the layout
#         layout.addWidget(self.label, 0, 0)
#         layout.addWidget(self.copy_button, 1, 0)

#         # Set the layout for the widget
#         self.setLayout(layout)

#     def copy_data(self):
#         # Get the text from the label
#         text = self.label.text()

#         # Copy the text to the clipboard
#         clipboard = QClipboard()
#         clipboard.setText(text)

# # Create an instance of the custom widget
# with open("logs.json", 'r') as f:
#     json_data = json.load(f)
# msg_box = CustomMessageBox(json_data)

# # Show the message box
# msg_box.show()
# msg_box.exec()