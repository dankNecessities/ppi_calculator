#!/usr/bin/env python3

from gui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow, UIMain):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setupUI(self)
		self.page1_button.clicked.connect(self.openPage1UI)
		self.page0_button.clicked.connect(self.openHomeUI)

		self.radiobutton1Q1.toggled.connect(self.on_q1_toggle)
		self.radiobutton1Q2.toggled.connect(self.on_q1_toggle)
		self.radiobutton1Q3.toggled.connect(self.on_q1_toggle)

	def openHomeUI(self):
		print("Back")
		self.QtStack.setCurrentIndex(0)

	def openPage1UI(self):
		print("Next")
		self.QtStack.setCurrentIndex(1)

	def on_q1_toggle(self):
		radiobutton = self.sender()

		if radiobutton.isChecked():
			print(radiobutton.figure)


if __name__ == '__main__':
	app = QApplication(sys.argv)
	s = Window()
	sys.exit(app.exec_())