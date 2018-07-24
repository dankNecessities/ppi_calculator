#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models import *
import sys, sqlite3, re

class defaultWindow(QWidget):
	def __init__(self, parent=None):
		super(defaultWindow, self).__init__(parent)
		self.setWindowTitle("Kamya's Poverty Index Calculator")
		self.setWindowIcon(QIcon('ppicon.png'))
		self.setObjectName('defWindow')
		self.resize(500, 600)
		self.setStyleSheet('''
			border-style: none;
			background-color: #101E41;
			''')
		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setSpacing(0)
		self.setLayout(self.layout)

class navBtn(QPushButton):
	def __init__(self, parent=None):
		super(navBtn, self).__init__(parent)
		self.setFlat(True)
		self.setMinimumSize(90, 30)
		self.setMaximumSize(90, 30)
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #20AE70;
			color: #20AE70;
			font-size: 15px;
			''')

	def enterEvent(self, QEvent):
		self.setStyleSheet('''
			background-color: #20AE70;
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #20AE70;
			color: #FFFFFF;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #20AE70;
			color: #20AE70;
			font-size: 15px;
			''')		

	def click_close(self):
		sys.exit()

class adminBtn(QPushButton):
	def __init__(self, parent=None):
		super(adminBtn, self).__init__(parent)
		self.setFlat(True)
		self.setMinimumSize(90, 30)
		self.setMaximumSize(90, 30)
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #ED1F0F;
			color: #ED1F0F;
			font-size: 15px;
			''')

	def enterEvent(self, QEvent):
		self.setStyleSheet('''
			background-color: #ED1F0F;
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #ED1F0F;
			color: #FFFFFF;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #ED1F0F;
			color: #ED1F0F;
			font-size: 15px;
			''')		

class uploadBtn(QPushButton):
	def __init__(self, parent=None):
		super(uploadBtn, self).__init__(parent)
		self.setFlat(True)
		self.setMinimumSize(90, 30)
		self.setMaximumSize(90, 30)
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #F3F61C;
			color: #F3F61C;
			font-size: 15px;
			''')

	def enterEvent(self, QEvent):
		self.setStyleSheet('''
			background-color: #F3F61C;
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #F3F61C;
			color: #000000;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Cambria";
			border-color: #F3F61C;
			color: #F3F61C;
			font-size: 15px;
			''')

class adminInput(QLineEdit):
	
	def __init__(self, parent=None):
		super(adminInput, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setContentsMargins(60, 0, 60, 0)
		self.setStyleSheet('''
			border-width: 0px 0px 2px 0px;
			border-style: solid;
			border-color: #ED1F0F;
			color: white;
			font-size: 15px;
			font-family: "Cambria";
			text-align: center;
			''')	

	def enterEvent(self, QEvent):
		self.setContentsMargins(40, 0, 40, 0)
		self.setStyleSheet('''
			border-width: 0px 0px 2px 0px;
			border-style: solid;
			border-color: #E55A4F;
			color: white;
			font-size: 15px;
			font-family: "Cambria";
			text-align: center;
			''')

	def leaveEvent(self, QEvent):
		self.setContentsMargins(60, 0, 60, 0)
		self.setStyleSheet('''
			border-width: 0px 0px 2px 0px;
			border-style: solid;
			border-color: #ED1F0F;
			color: white;
			font-size: 15px;
			font-family: "Cambria";
			text-align: center;
			''')

class Heading(QLabel):

	def __init__(self, parent=None):
		super(Heading, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet('''
			color: white;
			font-size: 55px;
			font-family: "Cambria";
			text-align: center;
			''')

class Description(QLabel):

	def __init__(self, parent=None):
		super(Description, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Cambria";
			color: #7CB7EF;
			''')

class BodyText(QLabel):
	def __init__(self, parent=None):
		super(BodyText, self).__init__(parent)
		self.setAlignment(Qt.AlignLeft)
		self.setContentsMargins(30, 0, 0, 0)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Cambria";
			color: #7CB7EF;
			''')
		self.setWordWrap(True)

class FieldText(QLabel):
	def __init__(self, parent=None):
		super(FieldText, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setContentsMargins(30, 0, 0, 0)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Cambria";
			color: #AAD1F4;
			''')
		self.setWordWrap(True)

class ResultText(QLabel):
	def __init__(self, parent=None):
		super(ResultText, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setContentsMargins(30, 0, 0, 0)
		self.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Cambria";
			color: #FCFF00;
			''')
		self.setWordWrap(True)

class PPIRadioButton(QRadioButton):
	def __init__(self, parent=None):
		super(PPIRadioButton, self).__init__(parent)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Cambria";
			color: #FFBF35;
			''')
		self.setText(self.wrapText(self.text(), 7))
	
	def wrapText(self, text, width):
		a = re.split(' ', text)
		p = ''
		i = 0
		limit = width - 1
		for q in a:
			if i < limit:
				p += q + ' '
			elif i == limit:
				p += q + '\n'
			elif i > limit:
				i = 0
				p += q + ' '
			i += 1
		return p

class RadioButtonGroup(QVBoxLayout):
	def __init__(self, parent=None):
		super(RadioButtonGroup, self).__init__(parent)
		self.setContentsMargins(30, 0, 0, 0)

class NationalityMenu(QComboBox):
	def __init__(self, parent=None):
		super(NationalityMenu, self).__init__(parent)
		self.setObjectName('nMenu')
		self.setStyleSheet('''QWidget#nMenu
			{	
				background-color: #117061;
				border-width: 2px 2px 2px 2px;
				border-style: solid;
				font-weight: bold;
				font-family: "Cambria";
				border-color: #FFFFFF;
				color: #FFFFFF;
				font-size: 15px;
			}
			''')

class UIMain(QWidget):
	def setupUI(self, Window):
		Window.resize(400, 400)

		self.QtStack = QStackedLayout()
		#new widget object for each window
		self.stack0 = defaultWindow()
		self.stack1 = defaultWindow()
		self.stack2 = defaultWindow()
		self.stack3 = defaultWindow()
		self.stack4 = defaultWindow()
		self.stack5 = defaultWindow()
		self.stack6 = defaultWindow()
		self.stack7 = defaultWindow()
		self.stack8 = defaultWindow()
		self.stack9 = defaultWindow()
		self.stack10 = defaultWindow()
		self.stack11 = defaultWindow()
		self.stack12 = defaultWindow()
		self.stack13 = defaultWindow()
		self.stack14 = defaultWindow()
		self.stack15 = defaultWindow()
		self.stack16 = defaultWindow()
		self.stack17 = defaultWindow()
		self.stack18 =  defaultWindow()

		self.setupHomeUI()
		self.QtStack.addWidget(self.stack0)
		
	def setupHomeUI(self):
		#Open database
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading("PPI Calculator")
		self.stack0.layout.addWidget(label1)

		#Description
		label2 = Description("About")
		label3 = BodyText("This program calculates the PPI of a household basing on the total score obtained after" \
			+ " completing our standardized questionnaire.")
		label4 = BodyText("Please select a country")
		self.stack0.layout.addWidget(label2)
		self.stack0.layout.addWidget(label3)
		self.stack0.layout.addWidget(label4)

		#Nationality Menu
		nbox = QGroupBox('')
		nhbox = QHBoxLayout()
		nhbox.setContentsMargins(100, 0, 100, 0)
		nbox.setLayout(nhbox)
		
		self.n_combobox = NationalityMenu(self)
		nats = conn.execute('SELECT NAME FROM NATIONALITIES;')
		for i in nats:
			self.n_combobox.addItem(i[0])
		
		nhbox.addWidget(self.n_combobox)
		self.stack0.layout.addWidget(nbox)

		#temp-> View results
		label5 = BodyText("View results")
		self.stack0.layout.addWidget(label5)

		udbox = QGroupBox('')
		udhbox = QHBoxLayout()
		udbox.setLayout(udhbox)

		upload_button = uploadBtn('Results')
		upload_button.clicked.connect(self.openViewPageUI)
		udhbox.setAlignment(Qt.AlignCenter)
		udhbox.addWidget(upload_button)
		self.stack0.layout.addWidget(udbox)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		admin_button = adminBtn("Admin")
		admin_button.clicked.connect(self.gotoLogin)
		homepage_next_button = navBtn("Next")
		homepage_next_button.clicked.connect(self.openBusinessPage)
		self.stack0.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(close_button)
		hbox.addWidget(admin_button)
		hbox.addWidget(homepage_next_button)

		#Close database
		conn.close()

	def setupBusinessPage(self):
		#Heading
		label1 = Heading("Business Name")
		self.stack18.layout.addWidget(label1)

		#Description
		label2 = BodyText("Create a business name below, or select one from the drop down list. Please note " \
			"that created businesses must be selected from the menu before continuing.")
		self.stack18.layout.addWidget(label2)

		#Business name menu
		nbox = QGroupBox('')
		nhbox = QHBoxLayout()
		nhbox.setContentsMargins(100, 0, 100, 0)
		nbox.setLayout(nhbox)

		conn = sqlite3.connect('testdb')
		
		self.biz_combobox = NationalityMenu(self)
		nats = conn.execute('SELECT NAME FROM BUSINESSES;')
		for i in nats:
			self.biz_combobox.addItem(i[0])
		
		self.biz_combobox.activated[str].connect(self.on_business_selection)
		nhbox.addWidget(self.biz_combobox)
		self.stack18.layout.addWidget(nbox)

		#Create business name box
		biz_box = QGroupBox()
		bizv_box = QVBoxLayout()
		biz_box.setLayout(bizv_box)

		biz = BodyText('New business name: ')
		self.business_name = adminInput()
		bizv_box.addWidget(biz)
		bizv_box.addWidget(self.business_name)
		self.stack18.layout.addWidget(biz_box)
		
		udbox = QGroupBox('')
		udhbox = QHBoxLayout()
		udbox.setLayout(udhbox)

		upload_button = uploadBtn('Create')
		upload_button.clicked.connect(self.createBusiness)
		udhbox.setAlignment(Qt.AlignCenter)
		udhbox.addWidget(upload_button)
		self.stack18.layout.addWidget(udbox)

		#Navigation buttons
		nav_gbox = QGroupBox('')
		hbox = QHBoxLayout()
		nav_gbox.setLayout(hbox)

		backbtn = navBtn('Back')
		closebtn = navBtn('Close')
		nextbtn = navBtn('Next')
		backbtn.clicked.connect(self.openHomeUI)
		closebtn.clicked.connect(navBtn.click_close)
		nextbtn.clicked.connect(self.openPage1UI)

		self.stack18.layout.addWidget(nav_gbox)
		hbox.setSpacing(50)
		hbox.addWidget(backbtn)
		hbox.addWidget(closebtn)
		hbox.addWidget(nextbtn)

		conn.close()

	def setupQuestionnairePage(self, stack, q_number, rbtn_function, backbtn, nextbtn):
		#Database Connect
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading('Questionnaire')
		stack.layout.addWidget(label1)

		#Description
		a = conn.execute('SELECT name FROM Questions WHERE parent="' + self.selected_nation + '" AND q_number=' + str(q_number))
		#print("Changed nation to: " + self.selected_nation)
		for i in a:
			qn1 = str(i[0])
		label2 = BodyText(qn1)
		stack.layout.addWidget(label2)

		#Radio button selection
		btn_gbox = QGroupBox('')
		vbox = RadioButtonGroup()
		btn_gbox.setLayout(vbox)
		stack.layout.addWidget(btn_gbox)
		b = conn.execute('SELECT * FROM Options WHERE parent="' + self.selected_nation + '" AND q_number=' + str(q_number))
		for i in b:
			option1 = str(i[0])
			radiobutton = PPIRadioButton(option1)
			radiobutton.figure = str(i[3])
			radiobutton.toggled.connect(rbtn_function)
			vbox.addWidget(radiobutton)
		radiobutton.setChecked(True)

		#Navigation buttons
		nav_gbox = QGroupBox('')
		hbox = QHBoxLayout()
		nav_gbox.setLayout(hbox)

		closebtn = navBtn('Close')
		closebtn.clicked.connect(navBtn.click_close)
		
		stack.layout.addWidget(nav_gbox)
		hbox.setSpacing(50)
		hbox.addWidget(backbtn)
		hbox.addWidget(closebtn)
		hbox.addWidget(nextbtn)

		#Database close
		conn.close()

	def setupResultPage(self):
		#Connect Database
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading("PPI Score")
		self.stack11.layout.addWidget(label1)

		#Description
		label2 = Description("How the index is calculated")
		label3 = BodyText("The PPI score is matched to a specific range depending on the selected nationality and percentile," \
			+ " to get the final index.")
		self.stack11.layout.addWidget(label2)
		self.stack11.layout.addWidget(label3)

		#Calculate PPI values
		self.sum_ppi_scores()
		self.get_ppi_index()

		#Result Boxes
		label4 = ResultText('Score: ' + str(self.ppi_score))
		self.stack11.layout.addWidget(label4)

		#Percentile Menu
		label5 = BodyText("Please select a percentile")
		self.stack11.layout.addWidget(label5)
		nbox = QGroupBox('')
		nhbox = QHBoxLayout()
		nhbox.setContentsMargins(100, 0, 100, 0)
		nbox.setLayout(nhbox)
		
		self.p_combobox = NationalityMenu(self)
		self.p_combobox.addItem('One Hundred')
		self.p_combobox.addItem('Two Hundred')
		self.p_combobox.addItem('Three Hundred')
		self.p_combobox.addItem('Poorest')
		self.p_combobox.activated[str].connect(self.on_percentile_selection)
		
		nhbox.addWidget(self.p_combobox)
		self.stack11.layout.addWidget(nbox)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openPage10UI)
		nextbtn = navBtn('Next')
		nextbtn.clicked.connect(self.openFinalPageUI)
		self.stack11.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(close_button)
		hbox.addWidget(nextbtn)

		#Close database
		conn.close()

	def setupFinalPage(self):
		#Heading
		label1 = Heading("Poverty Rate")
		self.stack12.layout.addWidget(label1)

		#Description
		label2 = Description("The Weighted Average Poverty Rate")
		label3 = BodyText("The PPI score is matched to a specific range depending on the selected nationality and" \
			" percentile, to get the poverty rate.")
		self.stack12.layout.addWidget(label2)
		self.stack12.layout.addWidget(label3)

		#Result Boxes
		label4 = ResultText('Poverty rate: ' + str(self.perc))
		self.stack12.layout.addWidget(label4)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openResultPageUI)
		nextbtn = navBtn('Next')
		nextbtn.clicked.connect(self.openViewPageUI)
		self.stack12.layout.addWidget(gbox)
		hbox.setSpacing(150)
		hbox.addWidget(backbtn)
		hbox.addWidget(close_button)		
		hbox.addWidget(nextbtn)

	def setupLogin(self):
		#Heading
		label1 = Heading("Administration")
		self.stack17.layout.addWidget(label1)

		#Description
		label3 = BodyText("Please enter your login credentials.")
		self.stack17.layout.addWidget(label3)

		#Login box
		#Username
		lbox1 = QGroupBox('')
		lhbox1 = QHBoxLayout()
		lbox1.setLayout(lhbox1)
		username = BodyText("Username: ")
		self.adminUser = adminInput()
		lhbox1.addWidget(username)
		lhbox1.addWidget(self.adminUser)

		#Password
		lbox2 = QGroupBox('')
		lhbox2 = QHBoxLayout()
		lbox2.setLayout(lhbox2)
		key = BodyText("Password: ")
		self.adminKey = adminInput()
		lhbox2.addWidget(key)
		lhbox2.addWidget(self.adminKey)

		lboxv = QGroupBox('')
		lvbox = QVBoxLayout()
		lboxv.setLayout(lvbox)

		#Error
		self.loginerror = BodyText("")
		
		lvbox.addWidget(lbox1)
		lvbox.addWidget(lbox2)
		lvbox.addWidget(self.loginerror)
		self.stack17.layout.addWidget(lboxv)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openHomeUI)
		nextbtn = navBtn('Login')
		nextbtn.clicked.connect(self.verifyLogin)
		self.stack17.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(nextbtn)

	def setupAdminPage1(self):
		#Heading
		label1 = Heading("Administration")
		self.stack13.layout.addWidget(label1)

		#Description
		label3 = BodyText("Create, modify and delete questions for selected countries.")
		self.stack13.layout.addWidget(label3)

		#Upload from spreadsheet
		label5 = BodyText("Upload country from spreadsheet: ")
		self.stack13.layout.addWidget(label5)

		udbox = QGroupBox('')
		udhbox = QHBoxLayout()
		udbox.setLayout(udhbox)

		upload_button = uploadBtn('Upload')
		upload_button.clicked.connect(self.openUploadPageUI)
		udhbox.setAlignment(Qt.AlignCenter)
		udhbox.addWidget(upload_button)
		self.stack13.layout.addWidget(udbox)

		#Replace question
		label4 = BodyText("Please select a Question to modify.")
		self.stack13.layout.addWidget(label4)

		nbox = QGroupBox('')
		nhbox = QHBoxLayout()
		nhbox.setContentsMargins(100, 0, 100, 0)
		nbox.setLayout(nhbox)
		
		self.u_combobox = NationalityMenu(self)
		self.u_combobox.addItem('One')
		self.u_combobox.addItem('Two')
		self.u_combobox.addItem('Three')
		self.u_combobox.addItem('Four')
		self.u_combobox.addItem('Five')
		self.u_combobox.addItem('Six')
		self.u_combobox.addItem('Seven')
		self.u_combobox.addItem('Eight')
		self.u_combobox.addItem('Nine')
		self.u_combobox.addItem('Ten')
		self.u_combobox.activated[str].connect(self.on_question_selection)
		
		nhbox.addWidget(self.u_combobox)
		self.stack13.layout.addWidget(nbox)

		#Question text
		label5 = BodyText("Please type the new question text")
		self.stack13.layout.addWidget(label5)

		self.insert_question = adminInput()
		self.stack13.layout.addWidget(self.insert_question)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		backbtn = navBtn('Logout')
		backbtn.clicked.connect(self.openHomeUI)
		updatebtn = adminBtn('Update')
		updatebtn.clicked.connect(self.replace_question)
		nextbtn = navBtn('Next')
		nextbtn.clicked.connect(self.openAdminPage2UI)
		self.stack13.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(updatebtn)
		hbox.addWidget(nextbtn)

	def setupAdminPage2(self):
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading("Administration")
		self.stack14.layout.addWidget(label1)

		#Description
		label3 = BodyText("Create, modify and delete response options for selected countries")
		self.stack14.layout.addWidget(label3)

		#Select Option
		label5 = BodyText("Please select an Option")
		self.stack14.layout.addWidget(label5)

		obox = QGroupBox('')
		ohbox = QHBoxLayout()
		ohbox.setContentsMargins(100, 0, 100, 0)
		obox.setLayout(ohbox)
		
		self.u2_combobox = NationalityMenu(self)
		self.u2_combobox.addItem('New Option')

		res = conn.execute('SELECT * FROM OPTIONS WHERE q_number=' + str(self.update_number) + ' AND parent="' + self.selected_nation + '";')
		for i in res:
			self.u2_combobox.addItem(i[0])
		self.u2_combobox.activated[str].connect(self.on_option_selection)
		
		ohbox.addWidget(self.u2_combobox)
		self.stack14.layout.addWidget(obox)		

		#Option text
		label6 = BodyText("Please type the new option text (0 to delete)")
		self.stack14.layout.addWidget(label6)

		self.insert_option = adminInput()
		self.stack14.layout.addWidget(self.insert_option)

		label7 = BodyText("Please type the new option value (integer)")
		self.stack14.layout.addWidget(label7)

		self.insert_option_val = adminInput()
		self.stack14.layout.addWidget(self.insert_option_val)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openAdminPage1UI)
		updatebtn = adminBtn('Update')
		updatebtn.clicked.connect(self.replace_option)
		nextbtn = navBtn('Home')
		nextbtn.clicked.connect(self.openHomeUI)
		self.stack14.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(updatebtn)
		hbox.addWidget(nextbtn)

	def setupUploadPageUI(self):
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading("Administration")
		self.stack15.layout.addWidget(label1)

		#Select File
		label3 = BodyText("Select file from which to upload Poverty index reference table")
		self.stack15.layout.addWidget(label3)
		
		fbox = QGroupBox('')
		fgbox = QHBoxLayout()
		fgbox.setSpacing(10)
		fbox.setLayout(fgbox)

		self.file_select = adminInput()
		upload = uploadBtn('Upload')
		upload.clicked.connect(self.openDialog)
		fgbox.addWidget(self.file_select)
		fgbox.addWidget(upload)

		self.stack15.layout.addWidget(fbox)

		#Name file
		label5 = BodyText("Please name the table, using its country identifier")
		self.stack15.layout.addWidget(label5)

		self.new_ppi_name = adminInput()
		self.stack15.layout.addWidget(self.new_ppi_name)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openHomeUI)
		updatebtn = adminBtn('Save')
		updatebtn.clicked.connect(self.add_new_ppi_table)
		self.stack15.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(updatebtn)

	def setupViewPageUI(self):
		#Heading
		label1 = Heading("Comparison")
		self.stack16.layout.addWidget(label1)

		#Description
		label2 = ResultText("Poverty Rates by business")
		self.stack16.layout.addWidget(label2)

		#Result Boxes
		stats = QGroupBox('')
		stat_box = QHBoxLayout()
		stat_box.setSpacing(10)
		stats.setLayout(stat_box)

		spacing = 30
		stat_names = QGroupBox('')
		stat_name_box = QVBoxLayout()
		stat_name_box.setSpacing(spacing)
		stat_names.setLayout(stat_name_box)
		stat_box.addWidget(stat_names)

		stat_values1 = QGroupBox('')
		stat_value_box1 = QVBoxLayout()
		stat_value_box1.setSpacing(spacing)
		stat_values1.setLayout(stat_value_box1)
		stat_box.addWidget(stat_values1)

		stat_values2 = QGroupBox('')
		stat_value_box2 = QVBoxLayout()
		stat_value_box2.setSpacing(spacing)
		stat_values2.setLayout(stat_value_box2)
		stat_box.addWidget(stat_values2)

		stat_values3 = QGroupBox('')
		stat_value_box3 = QVBoxLayout()
		stat_value_box3.setSpacing(spacing)
		stat_values3.setLayout(stat_value_box3)
		stat_box.addWidget(stat_values3)

		stat_values4 = QGroupBox('')
		stat_value_box4 = QVBoxLayout()
		stat_value_box4.setSpacing(spacing)
		stat_values4.setLayout(stat_value_box4)
		stat_box.addWidget(stat_values4)

		stat_values5 = QGroupBox('')
		stat_value_box5 = QVBoxLayout()
		stat_value_box5.setSpacing(spacing)
		stat_values5.setLayout(stat_value_box5)
		stat_box.addWidget(stat_values5)

		self.stack16.layout.addWidget(stats)

		stat_name_box.addWidget(FieldText('Business'))
		stat_value_box1.addWidget(FieldText('PPI '))
		stat_value_box2.addWidget(FieldText('1% '))
		stat_value_box3.addWidget(FieldText('2% '))
		stat_value_box4.addWidget(FieldText('3% '))
		stat_value_box5.addWidget(FieldText('4% '))

		results = self.getHouseholdAverages()

		for i in results:
			stat_business = i
			stat_name_box.addWidget(BodyText(str(stat_business)))
			stat_value_box1.addWidget(BodyText(str(results[i][0])))
			stat_value_box2.addWidget(BodyText(str(results[i][1])))
			stat_value_box3.addWidget(BodyText(str(results[i][2])))
			stat_value_box4.addWidget(BodyText(str(results[i][3])))
			stat_value_box5.addWidget(BodyText(str(results[i][4])))

		#Final weighted average poverty rate
		avg = self.getTotalAverage()
		label4 = ResultText('Weighted Average Poverty Rate')
		
		avgBox = QGroupBox('')
		avgVBox = QVBoxLayout()
		avgBox.setLayout(avgVBox)
		avgVBox.setSpacing(10)

		avgBox2 = QGroupBox('')
		avgHBox1 = QHBoxLayout()
		avgBox2.setLayout(avgHBox1)
		avgHBox1.addWidget(FieldText('Score'))
		avgHBox1.addWidget(FieldText('1% '))
		avgHBox1.addWidget(FieldText('2% '))
		avgHBox1.addWidget(FieldText('3% '))
		avgHBox1.addWidget(FieldText('4% '))

		avgBox3 = QGroupBox('')
		avgHBox2 = QHBoxLayout()
		avgBox3.setLayout(avgHBox2)
		try:
			avgHBox2.addWidget(BodyText(str(avg[0])))
			avgHBox2.addWidget(BodyText(str(avg[1])))
			avgHBox2.addWidget(BodyText(str(avg[2])))
			avgHBox2.addWidget(BodyText(str(avg[3])))
			avgHBox2.addWidget(BodyText(str(avg[4])))
		except IndexError as e:
			pass
		

		avgVBox.addWidget(avgBox2)
		avgVBox.addWidget(avgBox3)

		self.stack16.layout.addWidget(label4)
		self.stack16.layout.addWidget(avgBox)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		homebtn = navBtn('Home')
		homebtn.clicked.connect(self.openHomeUI)
		backbtn = navBtn('Back')
		backbtn.clicked.connect(self.openResultPageUI)
		self.stack16.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(backbtn)
		hbox.addWidget(homebtn)
		hbox.addWidget(close_button)

	def sum_ppi_scores(self):
		self.ppi_score = int(self.q1_answer) + int(self.q2_answer) + int(self.q3_answer) + int(self.q4_answer) + int(self.q5_answer)
		self.ppi_score += int(self.q6_answer) + int(self.q7_answer) + int(self.q8_answer) + int(self.q9_answer) + int(self.q10_answer)

	def get_ppi_index(self):
		conn = sqlite3.connect('testdb')

		res = conn.execute('SELECT * FROM ' + self.selected_nation)

		if self.ppi_score == 0:
			self.ppi_score = 4
		elif self.ppi_score == 100:
			self.ppi_score = 99

		for row in res:
			if 0 <= self.ppi_score - row[0] <= 4:
				ppi_index_one = row[1]
				ppi_index_two = row[2]
				ppi_index_three = row[3]
				ppi_index_four = row[4]

		if self.ppi_percentile == 'One Hundred':
			self.perc = ppi_index_one
			self.perc_val = 1
		elif self.ppi_percentile == 'Two Hundred':
			self.perc = ppi_index_two
			self.perc_val = 2
		elif self.ppi_percentile == 'Three Hundred':
			self.perc = ppi_index_three
			self.perc_val = 3
		elif self.ppi_percentile == 'Poorest':
			self.perc = ppi_index_four
			self.perc_val = 4

		res.close()
		
		index = wService('Households')
		index.insert_item(self.selected_business, self.ppi_score, ppi_index_one, ppi_index_two, ppi_index_three, \
		 ppi_index_four, self.selected_nation)
		conn.close()
		
	def openDialog(self):
		self.file_select.setText("")
		options = QFileDialog.Options()
		options |= QFileDialog.DontUseNativeDialog
		fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
		"All Files (*) ;;Spreadsheet Files (*.xlsx, *.xls)", options=options)
		if fileName:
			print(fileName)
			self.file_input = fileName
			self.file_select.setText(self.file_input)

	def getHouseholdAverages(self):
		conn = sqlite3.connect('testdb')
		res = conn.execute('SELECT * FROM BUSINESSES')
		res2 = conn.execute('SELECT * FROM households')
		result_dict = {}

		#Transfer to stable memory
		temp_list = []
		temp_list2 = []
		
		for i in res:
			temp_list.append(i)

		for i in res2:
			temp_list2.append(i)

		for i in temp_list:
			buff_list = []
			for j in temp_list2:
				if j[0] == i[0]:
					buff_list.append([j[1], j[2], j[3], j[4], j[5]])
			result_dict[i[0]] = buff_list
		
		print(result_dict)
		
		trans_dict = {}
		for i in result_dict:
			trans_dict[i] = []
			list1 = []
			list2 = []
			list3 = []
			list4 = []
			list5 = []
			for j in result_dict[i]:
				list1.append(j[0])
				list2.append(j[1])
				list3.append(j[2])
				list4.append(j[3])
				list5.append(j[4])
			trans_dict[i].append(list1)
			trans_dict[i].append(list2)
			trans_dict[i].append(list3)
			trans_dict[i].append(list4)
			trans_dict[i].append(list5)

		biz_weighted_no = 0
		final_dict = {}
		for i in trans_dict:
			final_dict[i] = []
			for j in trans_dict[i]:
				final_avg = self.getAvgFromList(j)
				final_dict[i].append(round(final_avg, 2))
			
			biz_no = len(trans_dict[i][0])
			biz_weighted_no += biz_no * final_avg

		print(final_dict)
		conn.close()
		return final_dict

	def getAvgFromList(self, some_list):
		n = len(some_list)
		sum = 0
		for item in some_list:
			sum += item
		if n != 0:
			average = sum/n
		else:
			average = 0
		return average

	def getTotalAverage(self):
		conn = sqlite3.connect('testdb')
		res = conn.execute('SELECT * FROM BUSINESSES')
		res2 = conn.execute('SELECT * FROM households')

		sum1 = 0
		sum2 = 0
		sum3 = 0
		sum4 = 0
		sum5 = 0
		for j in res2:
			sum1 += round(j[1], 2)
			sum2 += round(j[2], 2)
			sum3 += round(j[3], 2)
			sum4 += round(j[4], 2)
			sum5 += round(j[5], 2)
		
		sum_list = [sum1, sum2, sum3, sum4, sum5]

		res3 = conn.execute('SELECT * FROM households')
		b_len = 0
		for i in res:
			n = 0
			for j in res3:
				if j[0] == i[0] and n == 0:
					print("here")
					b_len += len(j)
					n = 1
			
		print(b_len)
		avg_list = []
		for k in sum_list:
			try:
				avg_list.append(round((k/b_len), 2))
			except ZeroDivisionError as e:
				pass
			

		conn.close()

		return avg_list
		