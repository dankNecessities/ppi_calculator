#!/usr/bin/env python3

from models import *
from gui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow, UIMain):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.selected_nation = 'Uganda'
		self.setupUI(self)
		self.page1_button.clicked.connect(self.openPage1UI)
		self.n_combobox.activated[str].connect(self.on_menu_selection)

	def openHomeUI(self):
		print("Back")
		self.QtStack.setCurrentWidget(self.stack1)

	def openPage1UI(self):
		print("Next")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack2)
		self.stack2 = defaultWindow()
		self.QtStack.addWidget(self.stack2)
		self.setupPage1UI()
		self.page0_button.clicked.connect(self.openHomeUI)
		self.QtStack.setCurrentWidget(self.stack2)

	def on_q1_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print(radiobutton.figure)

	def on_menu_selection(self):
		menuitem = self.sender()
		self.selected_nation = menuitem.currentText()
		print(self.selected_nation)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	s = Window()
	sys.exit(app.exec_())