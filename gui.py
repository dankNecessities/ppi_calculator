#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models import *
import sys, sqlite3

class defaultWindow(QWidget):
	def __init__(self, parent=None):
		super(defaultWindow, self).__init__(parent)
		self.setWindowTitle("Kamya's PPI Calculator")
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
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
			border-color: #20AE70;
			color: #FFFFFF;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Sawasdee";
			border-color: #20AE70;
			color: #20AE70;
			font-size: 15px;
			''')		

	def click_close(self):
		sys.exit()

class Heading(QLabel):

	def __init__(self, parent=None):
		super(Heading, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet('''
			color: white;
			font-size: 55px;
			font-family: "Sawasdee";
			text-align: center;
			''')

class Description(QLabel):

	def __init__(self, parent=None):
		super(Description, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')

class BodyText(QLabel):
	def __init__(self, parent=None):
		super(BodyText, self).__init__(parent)
		self.setAlignment(Qt.AlignCenter)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')
		self.setWordWrap(True)

class PPIRadioButton(QRadioButton):
	def __init__(self, parent=None):
		super(PPIRadioButton, self).__init__(parent)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')

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
				font-family: "Sawasdee";
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

		self.setupHomeUI()

		self.QtStack.addWidget(self.stack0)
		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		
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

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		self.homepage_next_button = navBtn("Next")
		self.stack0.layout.addWidget(gbox)
		hbox.setSpacing(150)
		hbox.addWidget(close_button)
		hbox.addWidget(self.homepage_next_button)

		#Close database
		conn.close()

	def setupPage1UI(self):
		#Database Connect
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading('Questionnaire')
		self.stack1.layout.addWidget(label1)

		#Description
		a = conn.execute('SELECT name FROM Questions WHERE parent="' + self.selected_nation + '" AND q_number=1')
		print("Changed nation to: " + self.selected_nation)
		for i in a:
			qn1 = str(i[0])
		label2 = BodyText(qn1)
		self.stack1.layout.addWidget(label2)

		#Radio button selection
		btn_gbox = QGroupBox('')
		vbox = RadioButtonGroup()
		btn_gbox.setLayout(vbox)
		self.stack1.layout.addWidget(btn_gbox)
		b = conn.execute('SELECT * FROM Options WHERE parent="' + self.selected_nation + '" AND q_number=1')
		for i in b:
			option1 = str(i[0])
			self.radiobuttonQ1 = PPIRadioButton(option1)
			self.radiobuttonQ1.figure = str(i[3])
			self.radiobuttonQ1.toggled.connect(self.on_q1_toggle)
			vbox.addWidget(self.radiobuttonQ1)
		self.radiobuttonQ1.setChecked(True)

		#Navigation buttons
		nav_gbox = QGroupBox('')
		hbox = QHBoxLayout()
		nav_gbox.setLayout(hbox)

		self.page1_back_button = navBtn('Back')
		close_button = navBtn('Close')
		close_button.clicked.connect(navBtn.click_close)
		self.page1_next_button = navBtn('Next')
		self.stack1.layout.addWidget(nav_gbox)
		hbox.setSpacing(50)
		hbox.addWidget(self.page1_back_button)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page1_next_button)

	def setupPage2UI(self):
		#Database Connect
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading('Questionnaire')
		self.stack2.layout.addWidget(label1)

		#Description
		a = conn.execute('SELECT name FROM Questions WHERE parent="' + self.selected_nation + '" AND q_number=2')
		print("Changed nation to: " + self.selected_nation)
		for i in a:
			qn1 = str(i[0])
		label2 = BodyText(qn1)
		self.stack2.layout.addWidget(label2)

		#Radio button selection
		btn_gbox = QGroupBox('')
		vbox = RadioButtonGroup()
		btn_gbox.setLayout(vbox)
		self.stack2.layout.addWidget(btn_gbox)
		b = conn.execute('SELECT * FROM Options WHERE parent="' + self.selected_nation + '" AND q_number=2')
		for i in b:
			option1 = str(i[0])
			self.radiobuttonQ2 = PPIRadioButton(option1)
			self.radiobuttonQ2.figure = str(i[3])
			self.radiobuttonQ2.toggled.connect(self.on_q2_toggle)
			vbox.addWidget(self.radiobuttonQ2)
		self.radiobuttonQ2.setChecked(True)

		#Navigation buttons
		nav_gbox = QGroupBox('')
		hbox = QHBoxLayout()
		nav_gbox.setLayout(hbox)

		self.page2_back_button = navBtn('Back')
		close_button = navBtn('Close')
		close_button.clicked.connect(navBtn.click_close)
		self.page2_next_button = navBtn('Next')
		self.stack2.layout.addWidget(nav_gbox)
		hbox.setSpacing(50)
		hbox.addWidget(self.page2_back_button)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page2_next_button)

	def setupPage3UI(self):
		#Database Connect
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading('Questionnaire')
		self.stack3.layout.addWidget(label1)

		#Description
		a = conn.execute('SELECT name FROM Questions WHERE parent="' + self.selected_nation + '" AND q_number=3')
		print("Changed nation to: " + self.selected_nation)
		for i in a:
			qn1 = str(i[0])
		label2 = BodyText(qn1)
		self.stack3.layout.addWidget(label2)

		#Radio button selection
		btn_gbox = QGroupBox('')
		vbox = RadioButtonGroup()
		btn_gbox.setLayout(vbox)
		self.stack3.layout.addWidget(btn_gbox)
		b = conn.execute('SELECT * FROM Options WHERE parent="' + self.selected_nation + '" AND q_number=3')
		for i in b:
			option1 = str(i[0])
			self.radiobuttonQ3 = PPIRadioButton(option1)
			self.radiobuttonQ3.figure = str(i[3])
			self.radiobuttonQ3.toggled.connect(self.on_q3_toggle)
			vbox.addWidget(self.radiobuttonQ3)
		self.radiobuttonQ3.setChecked(True)

		#Navigation buttons
		nav_gbox = QGroupBox('')
		hbox = QHBoxLayout()
		nav_gbox.setLayout(hbox)

		self.page3_back_button = navBtn('Back')
		close_button = navBtn('Close')
		close_button.clicked.connect(navBtn.click_close)
		self.page3_next_button = navBtn('Next')
		self.stack3.layout.addWidget(nav_gbox)
		hbox.setSpacing(50)
		hbox.addWidget(self.page3_back_button)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page3_next_button)