#!/usr/bin/env python3

from models import *
from gui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow, UIMain):
	def __init__(self, parent=None):
		super(Window, self).__init__(parent)
		self.selected_nation = 'Uganda'
		self.selected_business = 'Mid range business'
		self.no_submit = 1
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
		self.ppi_score = ''
		self.ppi_percentile = 'One Hundred'		
		self.ppi_index = ''
		self.update_number = 1
		self.update_option = ''
		self.setupUI(self)
		self.n_combobox.activated[str].connect(self.on_menu_selection)

	def openHomeUI(self):
		#Prevent resubmissions
		self.no_submit = 1

		print("Home")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack0)
		self.stack0 = defaultWindow()
		self.QtStack.addWidget(self.stack0)

		#Template generation
		self.setupHomeUI()
		self.QtStack.setCurrentWidget(self.stack0)

	def openPage1UI(self):
		#Prevent resubmissions
		self.no_submit = 0

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
		nextbtn.clicked.connect(self.openResultPageUI)

		#Generate page from template
		self.setupQuestionnairePage(self.stack10, 10, self.on_q10_toggle, backbtn, nextbtn)
		self.QtStack.setCurrentWidget(self.stack10)

	def openResultPageUI(self):
		print('Result Page')
		self.QtStack.removeWidget(self.stack11)
		self.stack11 = defaultWindow()
		self.QtStack.addWidget(self.stack11)

		#Template generation
		self.setupResultPage()
		self.QtStack.setCurrentWidget(self.stack11)

	def openFinalPageUI(self):
		print('Final Page')
		self.QtStack.removeWidget(self.stack12)
		self.stack12 = defaultWindow()
		self.QtStack.addWidget(self.stack12)

		#Template generation
		self.setupFinalPage()
		self.QtStack.setCurrentWidget(self.stack12)

	def openViewPageUI(self):
		print('View Page')
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack16)
		self.stack16 = defaultWindow()
		self.QtStack.addWidget(self.stack16)

		#Template generation
		self.setupViewPageUI()
		self.QtStack.setCurrentWidget(self.stack16)

	def gotoLogin(self):
		print('Login Page')
		self.QtStack.removeWidget(self.stack17)
		self.stack17 = defaultWindow()
		self.QtStack.addWidget(self.stack17)

		#Template generation
		self.setupLogin()
		self.QtStack.setCurrentWidget(self.stack17)

	def verifyLogin(self):
		print('Verifying Login')
		if self.adminUser.text() == "kamya" and self.adminKey.text() == "passkey":
			self.openAdminPage1UI()
		else:
			self.loginerror.setText("Username or Password incorrect!") 

	def openBusinessPage(self):
		print('Business Page')
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack18)
		self.stack18 = defaultWindow()
		self.QtStack.addWidget(self.stack18)		

		#Template generation
		self.setupBusinessPage()
		self.QtStack.setCurrentWidget(self.stack18)

	def openAdminPage1UI(self):
		print("Admin Page 1")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack13)
		self.stack13 = defaultWindow()
		self.QtStack.addWidget(self.stack13)		

		#Template generation
		self.setupAdminPage1()
		self.QtStack.setCurrentWidget(self.stack13)

	def openAdminPage2UI(self):
		print("Admin Page 2")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack14)
		self.stack14 = defaultWindow()
		self.QtStack.addWidget(self.stack14)		

		#Template generation
		self.setupAdminPage2()
		self.QtStack.setCurrentWidget(self.stack14)		

	def openUploadPageUI(self):
		print("Upload Page")
		#Remove and reinitialize old page
		self.QtStack.removeWidget(self.stack15)
		self.stack15 = defaultWindow()
		self.QtStack.addWidget(self.stack15)		

		#Template generation
		self.setupUploadPageUI()
		self.QtStack.setCurrentWidget(self.stack15)						

	def on_menu_selection(self):
		menuitem = self.sender()
		self.selected_nation = menuitem.currentText()
		print(self.selected_nation)

	def on_business_selection(self):
		menuitem = self.sender()
		self.selected_business = menuitem.currentText()
		print(self.selected_business)

	def on_percentile_selection(self):
		perc = self.sender()
		self.ppi_percentile = perc.currentText()
		print(self.ppi_percentile)
		self.get_ppi_index()

	def on_question_selection(self):
		qn = self.sender()
		qid = qn.currentText()
		if qid == "One":
			self.update_number = 1
		elif qid == "Two":
			self.update_number = 2
		elif qid == "Three":
			self.update_number = 3
		elif qid == "Four":
			self.update_number = 4
		elif qid == "Five":
			self.update_number = 5
		elif qid == "Six":
			self.update_number = 6
		elif qid == "Seven":
			self.update_number = 7
		elif qid == "Eight":
			self.update_number = 8
		elif qid == "Nine":
			self.update_number = 9
		elif qid == "Ten":
			self.update_number = 10

	def on_option_selection(self):
		opn = self.sender()
		self.update_option = opn.currentText()

	def replace_question(self):
		update_qn = self.insert_question.text()
		if len(update_qn) < 1:
			self.insert_question.setText("TOO SHORT!")	
		elif update_qn == 'TOO SHORT!':
			self.insert_question.setText("")	
		elif update_qn == 'SUCCESS!':
			self.insert_question.setText("")
		else:
			self.insert_question.setText("")
			qns = wService('Questions')
			qns.delete_item(parent=self.selected_nation, q_number=self.update_number)
			qns.insert_item(update_qn, self.selected_nation, self.update_number)
			self.insert_question.setText("SUCCESS!")

	def replace_option(self):
		update_qn = self.insert_option.text()
		update_val = self.insert_option_val.text()
		if len(update_qn) < 1:
			self.insert_question.setText("TOO SHORT!")	
		elif update_qn == 'TOO SHORT!':
			self.insert_question.setText("")
		elif update_qn == 'SUCCESS!':
			self.insert_question.setText("")
		else:
			qns = wService('Options')
			print(self.update_option)
			if self.update_option == 'New Option':
				self.insert_option.setText("")
				self.insert_option_val.setText("")
				qns.insert_item(update_qn, self.selected_nation, self.update_number, update_val)
				self.insert_option.setText("SUCCESS!")
			elif update_qn == '0':
				self.insert_option.setText("")
				self.insert_option_val.setText("")
				qns.delete_item(name=self.update_option, parent=self.selected_nation, q_number=self.update_number)
				self.insert_option.setText("DELETED!")
			else:
				self.insert_option.setText("")
				self.insert_option_val.setText("")
				qns.delete_item(name=self.update_option, parent=self.selected_nation, q_number=self.update_number)
				qns.insert_item(update_qn, self.selected_nation, self.update_number, update_val)
				self.insert_option.setText("SUCCESS!")
				self.insert_option_val.setText("SUCCESS!")

	def add_new_ppi_table(self):
		new_ppi = lookupService(self.new_ppi_name.text(), ppi_range='int', dOH='real', dTH='real', dThH='real', poorest='real')
		new_ppi.load_spreadsheet_values(self.file_select.text())
		self.new_ppi_name.setText("SUCCESS")

	def createBusiness(self):
		business = wService('Businesses')
		business.insert_item(self.business_name.text())
		self.openBusinessPage()

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