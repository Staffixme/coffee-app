import sys

from PyQt6.QtWidgets import QWidget, QTableWidget, QApplication
from PyQt6 import uic

import sqlite3

class CoffeeApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.initTable()

    def initTable(self):

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(["Сорт", "Обжарка", "Молотый/В зернах", "Вкус", "Цена", "Объем упаковки"])

        with sqlite3.connect("coffee.sqlite") as db:
            cur = db.cursor()
            data = cur.execute("""
            SELECT * FROM Coffee
            """).fetchall()

        self.tableWidget.setRowCount(len(data))

        for i in range(len(data) - 1):
            self.tableWidget.setItemLabel(i, 0, data[1])
            self.tableWidget.setItemLabel(i, 1, data[2])
            self.tableWidget.setItemLabel(i, 2, data[3])
            self.tableWidget.setItemLabel(i, 3, data[4])
            self.tableWidget.setItemLabel(i, 4, data[5])
            self.tableWidget.setItemLabel(i, 5, data[6])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    coffee_app = CoffeeApp()
    coffee_app.show()
    sys.exit(app.exec())