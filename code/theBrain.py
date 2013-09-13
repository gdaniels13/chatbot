from database import Database
from rule import Rule


class Brain:
	def __init__(self,name='Ida',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
		self.createRules()
	


	def setName(self,name):
		self.name=name
	


	def whatNext(self,statement):
		for x in self.Rules:
			if x.does_match_rule(statement):
				response = x.generate_response(statement)
				self.db.insertQA(statement,response)
				return response
				#perhaps add a rule to go back to a previous repsonse or question
		return "youre an imbecile"

	def createRules(self):
		self.Rules = []
		self.Rules.append( Rule( 'how [[does][do]]? (.*) make you feel' , "i feel happy about "))

		#must be the last rule
		self.Rules.append( Rule( '.*' , "you are a moron"))		