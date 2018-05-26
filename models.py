import sqlite3, pandas

class wService():

	#Specify property type on init
	def __init__(self, service_name, **kwargs):
		self.properties = []
		self.kw_properties = []
		self.create_statement = ''
		self.table_created = False
		
		self.entity_name = service_name
		self.__verify_existence__()
		if self.table_created == False:
			#Load properties if specified, Note: always placed in alphabetic order!
			if len(kwargs) > 0:
				self.__load_properties__(kwargs)
				self.__create_database_entries__()
		else:
			self.__get_properties__()			

	#Check whether the table already exists
	def __verify_existence__(self):
		try:
			conn = sqlite3.connect('testdb')
			res = conn.execute("SELECT * FROM EXISTING")
			for row in res:
				if str(row[0]) == str(self.entity_name):
					self.table_created = True
		except sqlite3.OperationalError as e:
			print(e)

	def __load_properties__(self, args):
		self.reset()
		self.kw_properties = args
		for i in args:
			self.properties.append(i)
		self.properties.sort()

	#Generate a sqlite create statement
	def __create_statement__(self):
		self.create_statement = 'CREATE TABLE ' + str(self.entity_name) + ' ('
		for i in self.kw_properties:
			if str(self.kw_properties[i]) == 'int':
				self.create_statement += '' + str(i) + ' INT NOT NULL, ' 
			elif str(self.kw_properties[i]) == 'real':
				self.create_statement += '' + str(i) + ' REAL NOT NULL, '
			elif str(self.kw_properties[i]) == 'text':
				self.create_statement += '' + str(i) + ' TEXT NOT NULL, '

		self.create_statement = self.create_statement[:-2]
		self.create_statement += ');'

	def __create_database_entries__(self):
		self.__create_statement__()
		conn = sqlite3.connect('testdb')
		try:
			conn.execute(self.create_statement)
			print("Table created")
			conn.execute('INSERT INTO EXISTING (NAME) VALUES ("' + str(self.entity_name) + '"); ')
			print("Table name added to existing")
			for i in self.properties:
				conn.execute('INSERT INTO PROPERTY_LIST (NAME, PARENT) VALUES ("'  + str(i) + '", "' \
					+ str(self.entity_name) + '" );')
			print('Properties added to property_list')
			conn.commit()
			self.table_created = True
		except sqlite3.OperationalError as e:
			print(e)
		conn.close()

	#Get properties from database
	def __get_properties__(self):
		self.reset()
		conn = sqlite3.connect('testdb')
		cursor = conn.execute('SELECT * FROM PROPERTY_LIST WHERE PARENT="' + str(self.entity_name) + '"; ')
		for row in cursor:
			self.properties.append(row[0])
		conn.close()

	def insert_item(self, *args):
		self.properties.sort()
		if len(args) == len(self.properties):
			conn = sqlite3.connect('testdb')
			insert_fields = ''
			insert_values = ''
			for i in self.properties:
				insert_fields += '"' + str(i) + '", '
			for j in args:
				insert_values += '"' + str(j) + '", '
			try:
				insert_statement = "INSERT INTO " + str(self.entity_name) + "( "
				insert_statement += insert_fields[:-2]
				insert_statement += ") VALUES ( "
				insert_statement += insert_values[:-2]
				insert_statement += ");"
				#print(insert_statement)
				conn.execute(insert_statement)
				conn.commit()
			except sqlite3.OperationalError as e:
				print("Insert failed!")
				print(e)		
			conn.close()
		else:
			print("Number of specified args does not match")

	def delete_item(self, item):
		conn = sqlite3.connect('testdb')
		try:
			conn.execute('DELETE FROM ' + str(self.entity_name) + ' WHERE ' + 'name="' + str(item) +  '";')
			conn.commit()
			print("Item :" + str(item) + " deleted")
		except sqlite3.OperationalError as e:
			print(e)

	def select_all_values(self):
		self.properties.sort()
		conn = sqlite3.connect('testdb')
		insert_fields = ''
		temp_props = ''
		for i in self.properties:
			insert_fields += str(i) + ", "
		try:
			temp_props = list(conn.execute("SELECT * FROM " + str(self.entity_name) + ";"))
		except sqlite3.OperationalError as e:
			pass
		conn.close()
		return temp_props

	def __create_json_body__(self, args):
		self.properties.sort()
		json_body = '['
		for i in args:
			temp_dict = {prop : value for prop, value in zip(self.properties, i)}
			json_body += json.dumps(temp_dict, sort_keys=True) + ', '
		json_body = json_body[:-2]
		json_body += ']'
		print(json_body)
		return(json_body)

	def load_json_body(self):
		vals = self.select_all_values()
		json_body = self.__create_json_body__(vals)
		return(json_body)

	def reset(self):
		self.properties = []

class lookupService(wService):
	def __create_database_entries__(self):
		self.__create_statement__()
		conn = sqlite3.connect('testdb')
		try:
			conn.execute(self.create_statement)
			print("Table created")
			conn.execute('INSERT INTO EXISTING (NAME) VALUES ("' + str(self.entity_name) + '"); ')
			conn.execute('INSERT INTO NATIONALITIES (NAME) VALUES ("' + str(self.entity_name) + '"); ')
			print("PPI name added to nationalities")
			print("Table name added to existing")
			for i in self.properties:
				conn.execute('INSERT INTO PROPERTY_LIST (NAME, PARENT) VALUES ("'  + str(i) + '", "' \
					+ str(self.entity_name) + '" );')
			print('Properties added to property_list')
			conn.commit()
			self.table_created = True
		except sqlite3.OperationalError as e:
			print(e)
		conn.close()

	def load_spreadsheet_values(self, sheetname):
		#load spreadsheet file
		if str(sheetname[-4:]) == 'xlsx' or str(sheetname[-3:]) == 'xls':
			ssf = pandas.read_excel(sheetname)
		elif(str(sheetname[-3:]) == 'csv'):
			ssf = pandas.read_csv(sheetname)
		try:
			ppi_range = ssf['Range']
			dOH = ssf['DoubleOneH']
			dTH = ssf['DoubleTwoH']
			dThH = ssf['DoubleThreeH']
			poorest = ssf['Poorest']

			for i in range(len(ppi_range)):
				self.insert_item(dOH[i], dTH[i], dThH[i], poorest[i], ppi_range[i])

		except NameError as e:
			print("The file is of the wrong format")

class SetupDatabase():
	def __init__(self):
		setup()

		#Create default PPI Tables
		default_ppi = lookupService('Uganda', ppi_range='int', dOH='real', dTH='real', dThH='real', poorest='real')
		default_ppi = lookupService('Kenya', ppi_range='int', dOH='real', dTH='real', dThH='real', poorest='real')
		default_ppi.load_spreadsheet_values('testPPIv2.xlsx')

		#Create Questions Table, insert default Questions
		Questions = wService('Questions', name='text', parent='text', q_number='int')
		Questions.insert_item('1. How many members does the household have?', 'Uganda', 1)
		Questions.insert_item('2. Are all household members ages 6 to 12 currently in school?', 'Uganda', 2)
		Questions.insert_item('3. Can the (oldest) female head/spouse read and write with understanding in any language?', 'Uganda', 3)
		Questions.insert_item('4. What type of material is mainly used for construction of the wall of the dwelling?', 'Uganda', 4)
		Questions.insert_item('5. What type of material is mainly used for construction of the roof of the dwelling?', 'Uganda', 5)

		Questions.insert_item('Kenyan locations', 'Kenya', 1)
		Questions.insert_item('Kenyan Foods', 'Kenya', 2)

		#Create Options
		Options = wService('Options', name='text', parent='text', q_number='int', value='int')
		#Question One
		Options.insert_item('Nine or more', 'Uganda', 1, 0)
		Options.insert_item('Eight', 'Uganda', 1, 3)
		Options.insert_item('Seven', 'Uganda', 1, 4)
		Options.insert_item('Five or Six', 'Uganda', 1, 6)
		Options.insert_item('Four', 'Uganda', 1, 8)
		Options.insert_item('Three', 'Uganda', 1, 12)
		Options.insert_item('Four', 'Uganda', 1, 8)
		Options.insert_item('Two', 'Uganda', 1, 21)
		Options.insert_item('One', 'Uganda', 1, 28)
		#Question Two
		Options.insert_item('No', 'Uganda', 2, 0)
		Options.insert_item('Yes', 'Uganda', 2, 2)
		Options.insert_item('No one currently ages 6 to 12', 'Uganda', 2, 5)
		#Question Three
		Options.insert_item('No', 'Uganda', 3, 0)
		Options.insert_item('No female head/spouse', 'Uganda', 3, 0)
		Options.insert_item('Yes', 'Uganda', 3, 3)
		#Question Four
		Options.insert_item('Unburnt bricks with mud, mud and poles or other', 'Uganda', 4, 0)
		Options.insert_item('Unburnt bricks with cement, wood, tin/iron sheets, concrete/stones, burnt stablilized bricks ' \
			+ 'or cement blocks', 'Uganda', 4, 4)
		#Question Five
		Options.insert_item('Thatch or tins', 'Uganda', 5, 0)
		Options.insert_item('Iron sheets, concrete, tiles, asbestos or other', 'Uganda', 5, 5)
		'''
		Options.insert_item('Matooke', 'Uganda', 2)
		Options.insert_item('Malakwang', 'Uganda', 2)

		Options.insert_item('Nairobi', 'Kenya', 1)
		Options.insert_item('Mombasa', 'Kenya', 1)
		Options.insert_item('Ugali', 'Kenya', 2)
		Options.insert_item('Beans', 'Kenya', 2)
		'''
		#Create Households Table
		Households = wService('Households', score='real', ppi_index='int', parent='text')

class setup():
	def __init__(self):
		#Setup
		try:
			conn = sqlite3.connect('testdb')
			conn.execute('CREATE TABLE EXISTING (NAME TEXT NOT NULL)')
			conn.execute('CREATE TABLE PROPERTY_LIST (NAME TEXT NOT NULL, PARENT TEXT NOT NULL)')
			conn.execute('CREATE TABLE NATIONALITIES (NAME TEXT NOT NULL)')
			conn.commit()
		except sqlite3.OperationalError as e:
			print(e)
		conn.close()

if __name__ == '__main__':
	SetupDatabase()