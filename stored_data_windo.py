import json

from PyQt6.QtCore import Qt, QAbstractTableModel,  QVariant
from PyQt6.QtWidgets import QMainWindow, QTableView

class MyTableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent):
        return len(self._data)

    def columnCount(self, parent):
        return len(self._data[0])

    def data(self, index, role):
        if role == Qt.ItemDataRole.DisplayRole:
            return self._data[index.row()][index.column()]

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return f"Column {section}"
            else:
                return f"Row {section}"



class StoredDataWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My Pop-Up Window")

        self.table_view = QTableView()
        self.setCentralWidget(self.table_view)

        with open("logs.json", "r") as f:
            self.data = json.load(f)

        for row in self.data:
            for item in row:
                item = [item]

        model = MyTableModel(self.data)
        self.table_view.setModel(model)

        self.show()

