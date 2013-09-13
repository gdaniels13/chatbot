import sqlite3

class Database:
	def __init__(self,dbName='memory.sqlite'):
		self.dbName=dbName
		self.conn = sqlite3.connect(dbName)
		self.cursor = self.conn.cursor()


	def insertQA(self,question,answer):
		qa = [(answer,question)]
		self.cursor.executemany('INSERT INTO responses values(?,?)',qa)
		self.conn.commit()
