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

class UIMain(QWidget):
	def setupUI(self, Window):
		Window.resize(400, 400)

		self.QtStack = QStackedLayout()
		#new widget object for each window
		self.stack1 = QWidget()
		self.stack2 = QWidget()

		self.setupHomeUI()
		self.setupPage1UI()

		self.QtStack.addWidget(self.stack1)
		self.QtStack.addWidget(self.stack2)
		
	def setupHomeUI(self):
		#self.setWindowTitle("Hello")
		self.stack1.resize(400, 400)
		self.stack1.setStyleSheet('''
				border-style: none;
				background-color: #101e41;
			''')
		layout = QVBoxLayout()
		layout.setContentsMargins(5, 5, 5, 5)
		layout.setSpacing(0)
		self.stack1.setLayout(layout)

		#Heading
		label1 = QLabel("PPI Calculator")
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label1.setStyleSheet('''
			color: white;
			font-size: 55px;
			font-family: "Sawasdee";
			text-align: center;
			''')
		layout.addWidget(label1)

		#Description
		label2 = QLabel("About")
		label2.setAlignment(QtCore.Qt.AlignCenter)
		label2.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')
		label3 = QLabel("This program calculates the PPI of a household basing on the total score obtained after" \
			+ " completing our standardized questionnaire.")
		label3.setAlignment(QtCore.Qt.AlignCenter)
		label3.setStyleSheet('''
			font-size: 15px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #7CB7EF;
			''')
		label3.setWordWrap(True)
		layout.addWidget(label2)
		layout.addWidget(label3)

		#Navigation buttons
		gbox = QGroupBox("")
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		self.page1_button = navBtn("Next")
		layout.addWidget(gbox)
		hbox.setSpacing(150)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page1_button)

	def setupPage1UI(self):
		self.stack2.resize(400, 400)
		self.stack2.setStyleSheet('''
				border-style: none;
				background-color: #101e41;
			''')
		layout = QVBoxLayout()
		layout.setContentsMargins(5, 5, 5, 5)
		layout.setSpacing(0)
		self.stack2.setLayout(layout)

		#Heading
		label1 = QLabel("Questionnaire")
		label1.setAlignment(QtCore.Qt.AlignCenter)
		label1.setStyleSheet('''
			color: white;
			font-size: 55px;
			font-family: "Sawasdee";
			text-align: center;
			''')
		layout.addWidget(label1)

		gbox = QGroupBox("")
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		self.page0_button = navBtn("Back")
		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		self.page2_button = navBtn("Next")
		layout.addWidget(gbox)
		hbox.setSpacing(50)
		hbox.addWidget(self.page0_button)
		hbox.addWidget(close_button)
		hbox.addWidget(self.page2_button)

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