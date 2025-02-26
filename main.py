import sqlite3
import sys

from PyQt6 import uic  # Импортируем uic
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddEditCoffee(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(800, 600)
		MainWindow.setMinimumSize(QtCore.QSize(800, 600))
		MainWindow.setMaximumSize(QtCore.QSize(800, 600))
		self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.label = QtWidgets.QLabel(parent=self.centralwidget)
		self.label.setGeometry(QtCore.QRect(160, 0, 201, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label.setFont(font)
		self.label.setAlignment(
			QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.label.setObjectName("label")
		self.l1 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l1.setGeometry(QtCore.QRect(410, 10, 181, 41))
		self.l1.setObjectName("l1")
		self.l2 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l2.setGeometry(QtCore.QRect(410, 80, 181, 41))
		self.l2.setObjectName("l2")
		self.l3 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l3.setGeometry(QtCore.QRect(410, 150, 181, 41))
		self.l3.setObjectName("l3")
		self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
		self.label_2.setGeometry(QtCore.QRect(160, 80, 181, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_2.setFont(font)
		self.label_2.setAlignment(
			QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.label_2.setObjectName("label_2")
		self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
		self.label_3.setGeometry(QtCore.QRect(160, 150, 181, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_3.setFont(font)
		self.label_3.setAlignment(
			QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.label_3.setObjectName("label_3")
		self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
		self.label_4.setGeometry(QtCore.QRect(160, 230, 191, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_4.setFont(font)
		self.label_4.setAlignment(
			QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
		self.label_4.setObjectName("label_4")
		self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
		self.label_5.setGeometry(QtCore.QRect(160, 310, 201, 51))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_5.setFont(font)
		self.label_5.setObjectName("label_5")
		self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
		self.label_6.setGeometry(QtCore.QRect(160, 400, 161, 41))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.label_6.setFont(font)
		self.label_6.setObjectName("label_6")
		self.l4 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l4.setGeometry(QtCore.QRect(410, 230, 181, 41))
		self.l4.setObjectName("l4")
		self.l5 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l5.setGeometry(QtCore.QRect(410, 320, 181, 41))
		self.l5.setObjectName("l5")
		self.l6 = QtWidgets.QLineEdit(parent=self.centralwidget)
		self.l6.setGeometry(QtCore.QRect(410, 400, 181, 41))
		self.l6.setObjectName("l6")
		self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(230, 470, 261, 61))
		font = QtGui.QFont()
		font.setPointSize(12)
		self.pushButton.setFont(font)
		self.pushButton.setStyleSheet("background-color: rgb(242, 255, 94);")
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.label.setText(_translate("MainWindow", "Название сорта"))
		self.label_2.setText(_translate("MainWindow", "Степень обжарки"))
		self.label_3.setText(_translate("MainWindow", "Молотый / в зернах"))
		self.label_4.setText(_translate("MainWindow", "Описание вкуса"))
		self.label_5.setText(_translate("MainWindow", "Цена"))
		self.label_6.setText(_translate("MainWindow", "Объём упаковки"))
		self.pushButton.setText(_translate("MainWindow", "Добавить запись"))


class Ui_MainWindow(object):
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(1000, 800)
		MainWindow.setMinimumSize(QtCore.QSize(1000, 800))
		MainWindow.setMaximumSize(QtCore.QSize(1000, 800))
		self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
		self.centralwidget.setObjectName("centralwidget")
		self.table = QtWidgets.QTableWidget(parent=self.centralwidget)
		self.table.setGeometry(QtCore.QRect(0, 0, 1000, 600))
		self.table.setObjectName("table")
		self.table.setColumnCount(0)
		self.table.setRowCount(0)
		self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
		self.pushButton.setGeometry(QtCore.QRect(210, 600, 500, 150))
		font = QtGui.QFont()
		font.setPointSize(18)
		self.pushButton.setFont(font)
		self.pushButton.setStyleSheet("background-color: rgb(255, 193, 69);")
		self.pushButton.setObjectName("pushButton")
		MainWindow.setCentralWidget(self.centralwidget)
		self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
		self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
		self.menubar.setObjectName("menubar")
		MainWindow.setMenuBar(self.menubar)
		self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
		self.statusbar.setObjectName("statusbar")
		MainWindow.setStatusBar(self.statusbar)

		self.retranslateUi(MainWindow)
		QtCore.QMetaObject.connectSlotsByName(MainWindow)

	def retranslateUi(self, MainWindow):
		_translate = QtCore.QCoreApplication.translate
		MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
		self.pushButton.setText(_translate("MainWindow", "Добавить запись"))


class AddWidget(QMainWindow, Ui_AddEditCoffee):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		self.pushButton.clicked.connect(self.act)

	def act(self):
		# Подключение к базе данных
		conn = sqlite3.connect('coffee.sqlite')
		cursor = conn.cursor()

		query = '''INSERT INTO table_for_coffee (class_name, step_objarki, ground_in_grains, taste_description, price, 
        volume) VALUES (?, ?, ?, ?, ?, ?)'''
		values = (
			self.l1.text(), self.l2.text(), self.l3.text(),
			self.l4.text(), self.l5.text(), self.l6.text())
		cursor.execute(query, values)

		# Сохранение изменений
		conn.commit()

		self.hide()
		self.mywidget = MyWidget()
		self.mywidget.show()


class MyWidget(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)

		connection = sqlite3.connect('data/coffee.sqlite')
		cursor = connection.cursor()

		query = '''SELECT * FROM table_for_coffee'''
		result = cursor.execute(query).fetchall()[::-1]

		self.table.setRowCount(len(result))
		self.table.setColumnCount(7)

		# Закрашиваем шапку таблицы (горизонтальные заголовки)
		self.table.horizontalHeader().setStyleSheet(
			"QHeaderView::section { background-color: rgb(255, 170, 127);}")

		# Закрашиваем боковую шапку таблицы (вертикальные заголовки)
		self.table.verticalHeader().setStyleSheet(
			"QHeaderView::section { background-color: rgb(255, 170, 127);}")

		# Устанавливаем заголовки столбцов
		header_labels = ['ID', 'Название_сорта', 'Степень_обжарки', 'Молотый/в_зернах', 'Описание_вкуса', 'Цена',
						 'Объём_упаковки']
		self.table.setHorizontalHeaderLabels(header_labels)

		self.table.horizontalHeader().setStretchLastSection(True)

		for i, elem in enumerate(result):
			for j, val in enumerate(elem):
				item = QTableWidgetItem(str(val))
				item.setBackground(QColor(85, 255, 255))
				self.table.setItem(i, j, item)
				if j == 0:
					item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)

		connection.close()

		# Подключение сигнала изменения ячейки
		self.table.itemChanged.connect(self.update_database)
		self.pushButton.clicked.connect(self.act)

	def act(self):
		self.hide()
		self.addwidget = AddWidget()
		self.addwidget.show()

	def update_database(self, item):
		row = item.row()
		column = item.column()
		value = item.text()

		connection = sqlite3.connect('coffee.sqlite')
		# Обновление базы данных
		cursor = connection.cursor()
		if column == 1:  # Если изменено имя
			cursor.execute("UPDATE table_for_coffee SET class_name = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		elif column == 2:  # Если изменен возраст
			cursor.execute("UPDATE table_for_coffee SET step_objarki = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		elif column == 3:  # Если изменен возраст
			cursor.execute("UPDATE table_for_coffee SET ground_in_grains = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		elif column == 4:  # Если изменен возраст
			cursor.execute("UPDATE table_for_coffee SET taste_description = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		elif column == 5:  # Если изменен возраст
			cursor.execute("UPDATE table_for_coffee SET price = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		else:  # Если изменен возраст
			cursor.execute("UPDATE table_for_coffee SET volume = ? WHERE ID = ?",
						   (value, self.table.item(row, 0).text()))
		connection.commit()


def except_hook(cls, exception, traceback):
	sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MyWidget()
	ex.show()
	sys.excepthook = except_hook
	sys.exit(app.exec())
