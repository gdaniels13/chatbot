from database import Database

class Brain:
	def __init__(self,name='freddy',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
	def setName(self,name):
		self.name=name
	def whatNext(self,statement):
		self.db.insertQA(statement,statement)
		return statement