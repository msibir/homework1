import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Название сорта", "Степень обжарки",
                                                "Молотый/в зернах", "Описание вкуса",
                                                "Цена", "Объем упаковки"])
        self.con = sqlite3.connect("coffee.sqlite")
        self.cur = self.con.cursor()
        a = self.cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(a))
        for i in range(len(a)):
            for j in range(7):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(a[i][j])))
        self.cur.close()
        self.con.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())