#!/usr/bin/env python3

from models import *
from gui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow, UIMain):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.selected_nation = 'Uganda'
		self.q1_answer = ''
		self.q2_answer = ''
		self.q3_answer = ''
		self.setupUI(self)
		self.homepage_next_button.clicked.connect(self.openPage1UI)
		self.n_combobox.activated[str].connect(self.on_menu_selection)

	def openHomeUI(self):
		print("Back")
		self.QtStack.setCurrentWidget(self.stack0)

	def openPage1UI(self):
		print("Page 1")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack1)
		self.stack1 = defaultWindow()
		self.QtStack.addWidget(self.stack1)
		self.setupPage1UI()
		self.page1_back_button.clicked.connect(self.openHomeUI)
		self.page1_next_button.clicked.connect(self.openPage2UI)
		self.QtStack.setCurrentWidget(self.stack1)

	def openPage2UI(self):
		print("Page 2")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack2)
		self.stack2 = defaultWindow()
		self.QtStack.addWidget(self.stack2)
		self.setupPage2UI()
		self.page2_back_button.clicked.connect(self.openPage1UI)
		self.page2_next_button.clicked.connect(self.openPage3UI)
		self.QtStack.setCurrentWidget(self.stack2)

	def openPage3UI(self):
		print("Page 3")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack3)
		self.stack3 = defaultWindow()
		self.QtStack.addWidget(self.stack3)
		self.setupPage3UI()
		self.page3_back_button.clicked.connect(self.openPage2UI)
		self.QtStack.setCurrentWidget(self.stack3)

	def on_q1_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 1')
			self.q1_answer = radiobutton.figure
			print(self.q1_answer)

	def on_q2_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 2')
			self.q2_answer = radiobutton.figure
			print(self.q2_answer)

	def on_q3_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 3')
			self.q3_answer = radiobutton.figure
			print(self.q3_answer)

	def on_menu_selection(self):
		menuitem = self.sender()
		self.selected_nation = menuitem.currentText()
		print(self.selected_nation)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	s = Window()
	sys.exit(app.exec_())