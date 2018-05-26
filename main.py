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
		self.q4_answer = ''
		self.q5_answer = ''
		self.q6_answer = ''
		self.q7_answer = ''
		self.q8_answer = ''
		self.q9_answer = ''
		self.q10_answer = ''
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
		
		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openHomeUI)
		nextbtn.clicked.connect(self.openPage2UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack1, 1, self.on_q1_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack1)

	def openPage2UI(self):
		print("Page 2")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack2)
		self.stack2 = defaultWindow()
		self.QtStack.addWidget(self.stack2)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage1UI)
		nextbtn.clicked.connect(self.openPage3UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack2, 2, self.on_q2_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack2)

	def openPage3UI(self):
		print("Page 3")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack3)
		self.stack3 = defaultWindow()
		self.QtStack.addWidget(self.stack3)
		
		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage2UI)
		nextbtn.clicked.connect(self.openPage4UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack3, 3, self.on_q3_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack3)

	def openPage4UI(self):
		print("Page 4")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack4)
		self.stack4 = defaultWindow()
		self.QtStack.addWidget(self.stack4)
		
		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage3UI)
		nextbtn.clicked.connect(self.openPage5UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack4, 4, self.on_q4_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack4)

	def openPage5UI(self):
		print("Page 5")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack5)
		self.stack5 = defaultWindow()
		self.QtStack.addWidget(self.stack5)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage4UI)
		nextbtn.clicked.connect(self.openPage6UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack5, 5, self.on_q5_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack5)

	def openPage6UI(self):
		print("Page 6")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack6)
		self.stack6 = defaultWindow()
		self.QtStack.addWidget(self.stack6)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage5UI)
		nextbtn.clicked.connect(self.openPage7UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack6, 6, self.on_q6_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack6)

	def openPage7UI(self):
		print("Page 7")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack7)
		self.stack7 = defaultWindow()
		self.QtStack.addWidget(self.stack7)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage6UI)
		nextbtn.clicked.connect(self.openPage8UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack7, 7, self.on_q7_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack7)

	def openPage8UI(self):
		print("Page 8")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack8)
		self.stack8 = defaultWindow()
		self.QtStack.addWidget(self.stack8)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage7UI)
		nextbtn.clicked.connect(self.openPage9UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack8, 8, self.on_q8_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack8)

	def openPage9UI(self):
		print("Page 9")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack9)
		self.stack9 = defaultWindow()
		self.QtStack.addWidget(self.stack9)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage8UI)
		nextbtn.clicked.connect(self.openPage10UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack9, 9, self.on_q9_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack9)

	def openPage10UI(self):
		print("Page 10")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack10)
		self.stack10 = defaultWindow()
		self.QtStack.addWidget(self.stack10)

		#Create variables for template
		backbtn = navBtn('Back')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openPage9UI)
		#nextbtn.clicked.connect(self.openPage9UI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack10, 10, self.on_q10_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack10)

	def on_menu_selection(self):
		menuitem = self.sender()
		self.selected_nation = menuitem.currentText()
		print(self.selected_nation)

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

	def on_q4_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 4')
			self.q4_answer = radiobutton.figure
			print(self.q4_answer)

	def on_q5_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 5')
			self.q5_answer = radiobutton.figure
			print(self.q5_answer)

	def on_q6_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 6')
			self.q6_answer = radiobutton.figure
			print(self.q6_answer)

	def on_q7_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 7')
			self.q7_answer = radiobutton.figure
			print(self.q7_answer)

	def on_q8_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 8')
			self.q8_answer = radiobutton.figure
			print(self.q8_answer)

	def on_q9_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 9')
			self.q9_answer = radiobutton.figure
			print(self.q9_answer)

	def on_q10_toggle(self):
		radiobutton = self.sender()
		if radiobutton.isChecked():
			print('Question 10')
			self.q10_answer = radiobutton.figure
			print(self.q10_answer)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	s = Window()
	sys.exit(app.exec_())