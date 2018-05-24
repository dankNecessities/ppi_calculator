#!/usr/bin/env python3

from models import *
from gui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow, UIMain):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.setupUI(self)
		self.page1_button.clicked.connect(self.openPage1UI)
		self.page0_button.clicked.connect(self.openHomeUI)

	def openHomeUI(self):
		print("Back")
		self.QtStack.setCurrentIndex(0)

	def openPage1UI(self):
		print("Next")
		self.QtStack.setCurrentIndex(1)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	s = Window()
	sys.exit(app.exec_())