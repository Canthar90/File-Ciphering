import json

from PyQt6.QtCore import Qt, QAbstractTableModel, QVariant
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableView, QTextEdit, QTextBrowser

# class MyTableModel(QAbstractTableModel):
#     def __init__(self, data):
#         super().__init__()
#         self._data = data

#     def rowCount(self, parent):
#         return len(self._data)

#     def columnCount(self, parent):
#         return len(self._data[0])

#     def data(self, index, role):
#         if role == Qt.ItemDataRole.DisplayRole:
#             return self._data[index.row()][index.column()]

#     def headerData(self, section, orientation, role):
#         if role == Qt.ItemDataRole.DisplayRole:
#             if orientation == Qt.Orientation.Horizontal:
#                 return f"Column {section}"
#             else:
#                 return f"Row {section}"

# class MyMainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("My Pop-Up Window")

#         self.table_view = QTableView()
#         self.setCentralWidget(self.table_view)

#         # Create some test data
#         data = [
#             [
#                 {
#                     "Item name": "test",
#                     "Date of encoding": "28:02:2024-15:50",
#                     "Encoding key": "HBapOmAuNa43EJ/yGr4HFQ=="
#                 },
#                 {
#                     "Item name": "test",
#                     "Date of encoding": "28:02:2024-15:52",
#                     "Encoding key": "czafevNKOdlxTSuqhI0/Kg=="
#                 }
#             ]
#         ]

#         # Modify the JSON data to be a list of lists of dictionaries
#         for row in data:
#             for item in row:
#                 item = [item]

#         model = MyTableModel(data)
#         self.table_view.setModel(model)

#         self.show()

# if __name__ == "__main__":
#     import sys

#     app = QApplication(sys.argv)
#     window = MyMainWindow()
#     app.exec()


# import json



if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    with open('logs.json', 'r')as f:
        s= json.load(f)
    # s = {"name": "Gilbert", "wins": [["straight", "7"], ["one pair", "10"]]}
    js = json.dumps(s, indent=4, sort_keys=True)
    w = QTextBrowser()
    w.setText(js)
    w.show()
    sys.exit(app.exec())