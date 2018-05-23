#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
import sys

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
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setStyleSheet('''
			color: white;
			font-size: 55px;
			font-family: "Sawasdee";
			text-align: center;
			''')

class Description(QLabel):

	def __init__(self, parent=None):
		super(Description, self).__init__(parent)
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')

class BodyText(QLabel):
	def __init__(self, parent=None):
		super(BodyText, self).__init__(parent)
		self.setAlignment(QtCore.Qt.AlignCenter)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')
		self.setWordWrap(True)

class defaultWindow(QWidget):
	def __init__(self, parent=None):
		super(defaultWindow, self).__init__(parent)
		self.resize(400, 400)
		self.setStyleSheet('''
				border-style: none;
				background-color: #101e41;
			''')
		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setSpacing(0)
		self.setLayout(self.layout)

class RadioButtonQ1(QRadioButton):
	def __init__(self, parent=None):
		super(RadioButtonQ1, self).__init__(parent)
		self.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')


class UIMain(QWidget):
	def setupUI(self, Window):
		Window.resize(400, 400)

		self.QtStack = QStackedLayout()
		#new widget object for each window
		self.stack1 = defaultWindow()
		self.stack2 = defaultWindow()

		self.setupHomeUI()
		self.setupPage1UI()

		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		
	def setupHomeUI(self):
		#self.setWindowTitle("Hello")

		#Heading
		label1 = Heading("PPI Calculator")
		self.stack1.layout.addWidget(label1)

		#Description
		label2 = Description("About")
		label3 = BodyText("This program calculates the PPI of a household basing on the total score obtained after" \
			+ " completing our standardized questionnaire.")
		
		self.stack1.layout.addWidget(label2)
		self.stack1.layout.addWidget(label3)

		#Navigation buttons
		gbox = QGroupBox("")
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		self.page1_button = navBtn("Next")
		self.stack1.layout.addWidget(gbox)
		hbox.setSpacing(150)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page1_button)

	def setupPage1UI(self):
		#Heading
		label1 = Heading("Questionnaire")
		self.stack2.layout.addWidget(label1)

		#Description
		label2 = BodyText("Click on the option that best represents your response.")
		self.stack2.layout.addWidget(label2)

		#Radio button selection
		self.Q1answer = ''
		self.radiobutton1Q1 = RadioButtonQ1("Brazil")

		self.radiobutton1Q1.setChecked(True)
		self.radiobutton1Q1.figure = "Square"
		self.stack2.layout.addWidget(self.radiobutton1Q1)

		self.radiobutton1Q2 = RadioButtonQ1("France")
		self.radiobutton1Q2.figure = "Triangle"
		self.stack2.layout.addWidget(self.radiobutton1Q2)

		self.radiobutton1Q3 = RadioButtonQ1("Germany")
		self.radiobutton1Q3.figure = "Circle"
		self.stack2.layout.addWidget(self.radiobutton1Q3)

		#Navigation buttons
		gbox = QGroupBox("")
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		self.page0_button = navBtn("Back")
		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		self.page2_button = navBtn("Next")
		self.stack2.layout.addWidget(gbox)
		hbox.setSpacing(50)
		hbox.addWidget(self.page0_button)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page2_button)