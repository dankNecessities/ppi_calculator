#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models import *
import sys, sqlite3, re

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
		self.setAlignment(Qt.AlignLeft)
		self.setContentsMargins(30, 0, 0, 0)
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
		self.stack4 = defaultWindow()
		self.stack5 = defaultWindow()
		self.stack6 = defaultWindow()
		self.stack7 = defaultWindow()
		self.stack8 = defaultWindow()
		self.stack9 = defaultWindow()
		self.stack10 = defaultWindow()

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

	def setupQuestionnairePage(self, stack, q_number, rbtn_function, backbtn, nextbtn):
		#Database Connect
		conn = sqlite3.connect('testdb')

		#Heading
		label1 = Heading('Questionnaire')
		stack.layout.addWidget(label1)

		#Description
		a = conn.execute('SELECT name FROM Questions WHERE parent="' + self.selected_nation + '" AND q_number=' + str(q_number))
		print("Changed nation to: " + self.selected_nation)
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