#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from models import *
import sys, sqlite3, re

class defaultWindow(QWidget):
	width = 500
	height = 600

	def __init__(self, parent=None):
		super(defaultWindow, self).__init__(parent)
		self.setWindowTitle("Kamya's Poverty Index Calculator")
		self.setWindowIcon(QIcon("ppicon.png"))
		self.setObjectName('defWindow')
		self.resize(self.width, self.height)
		self.setStyleSheet('''
			border-style: none;
			background-color: #101E41;
			''')
		self.layout = QVBoxLayout()
		self.layout.setContentsMargins(5, 5, 5, 5)
		self.layout.setSpacing(0)
		self.setLayout(self.layout)
		self.center_window()

	def center_window(self):
		screen = QDesktopWidget()
		screen_width = screen.width()
		screen_height = screen.height()
		h_pos = (screen_width - self.width)	/ 2
		v_pos = (screen_height - self.height) / 2
		self.move(h_pos,v_pos)

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
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
			border-color: #ED1F0F;
			color: #FFFFFF;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
			border-color: #F3F61C;
			color: #000000;
			font-size: 15px;
			''')

	def leaveEvent(self, QEvent):
		self.setStyleSheet('''
			border-width: 2px 2px 2px 2px;
			border-style: solid;
			font-weight: bold;
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
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
			font-family: "Sawasdee";
			text-align: center;
			''')

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

class ResultText(QLabel):
	def __init__(self, parent=None):
		super(ResultText, self).__init__(parent)
		self.setAlignment(Qt.AlignLeft)
		self.setContentsMargins(30, 0, 0, 0)
		self.setStyleSheet('''
			font-size: 30px;
			font-weight: bold;
			font-family: "Sawasdee";
			color: #FCFF00;
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
		self.stack11 = defaultWindow()
		self.stack12 = defaultWindow()
		self.stack13 = defaultWindow()
		self.stack14 = defaultWindow()
		self.stack15 = defaultWindow()
		self.stack16 = defaultWindow()

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

		#Upload from spreadsheet
		udbox = QGroupBox('')
		udvbox = QVBoxLayout()
		udbox.setLayout(udvbox)

		label5 = BodyText("Or: ")
		label5.setContentsMargins(20, 0, 0, 0)
		upload_button = uploadBtn('Upload')
		upload_button.clicked.connect(self.openUploadPageUI)
		udvbox.setAlignment(Qt.AlignCenter)
		udvbox.addWidget(label5)
		udvbox.addWidget(upload_button)

		self.stack0.layout.addWidget(udbox)

		#Navigation buttons
		gbox = QGroupBox('')
		hbox = QHBoxLayout()
		gbox.setLayout(hbox)

		close_button = navBtn("Close")
		close_button.clicked.connect(navBtn.click_close)
		admin_button = adminBtn("Admin")
		admin_button.clicked.connect(self.openAdminPage1UI)
		homepage_next_button = navBtn("Next")
		homepage_next_button.clicked.connect(self.openPage1UI)
		self.stack0.layout.addWidget(gbox)
		hbox.setSpacing(70)
		hbox.addWidget(close_button)
		hbox.addWidget(admin_button)
		hbox.addWidget(homepage_next_button)

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
		label1 = Heading("PPI Index")
		self.stack12.layout.addWidget(label1)

		#Description
		label2 = Description("The Poverty Probability index")
		label3 = BodyText("The PPI score is matched to a specific range depending on the selected nationality and percentile," \
			+ " to get the final index.")
		self.stack12.layout.addWidget(label2)
		self.stack12.layout.addWidget(label3)

		#Result Boxes
		label4 = ResultText('Final index: ' + str(self.perc))
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

	def setupAdminPage1(self):
		#Heading
		label1 = Heading("Administration")
		self.stack13.layout.addWidget(label1)

		#Description
		label3 = BodyText("Create, modify and delete questions for selected countries")
		self.stack13.layout.addWidget(label3)

		#Replace question
		label4 = BodyText("Please select a Question")
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

		backbtn = navBtn('Back')
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
		label2 = BodyText("The Poverty Probability index averages compared by country")
		self.stack16.layout.addWidget(label2)

		#Result Boxes
		stats = QGroupBox('')
		stat_box = QHBoxLayout()
		stat_box.setSpacing(70)
		stats.setLayout(stat_box)

		stat_names = QGroupBox('')
		stat_name_box = QVBoxLayout()
		stat_name_box.setSpacing(70)
		stat_names.setLayout(stat_name_box)
		stat_box.addWidget(stat_names)

		stat_values = QGroupBox('')
		stat_value_box = QVBoxLayout()
		stat_value_box.setSpacing(70)
		stat_values.setLayout(stat_value_box)
		stat_box.addWidget(stat_values)

		self.stack16.layout.addWidget(stats)

		stat_name_box.addWidget(BodyText('Country'))
		stat_value_box.addWidget(BodyText('Values'))

		results = self.getHouseholdAverages()

		for i in results:
			stat_country = i
			stat_value = results[i]
			stat_name_box.addWidget(BodyText(str(stat_country)))
			stat_value_box.addWidget(BodyText(str(stat_value)))

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

		#res = conn.execute('SELECT ppi_range, ' + perc + ' FROM ' + self.selected_nation)
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
		index.insert_item(self.ppi_score, ppi_index_one, ppi_index_two, ppi_index_three, ppi_index_four, self.selected_nation)
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
		res = conn.execute('SELECT * FROM NATIONALITIES')
		res2 = conn.execute('SELECT * FROM households')
		result_dict = {}
		for i in res:
			temp_list = []
			for j in res2:
				if j[5] == i[0]:
					temp_list.append(int(j[self.perc_val]))
			result_dict[i[0]] = temp_list
			print(temp_list)
		averages_dict = {}
		for i in result_dict:
			avg = self.getAvgFromList(result_dict[i])
			averages_dict[i] = avg

		return averages_dict

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