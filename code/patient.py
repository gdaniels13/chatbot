import sys
import os
from database import Database
from rule import Rule


class Patient:
	def __init__(self,name='Ida',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
		self.create_rules()
	


	def set_name(self,name):
		self.name=name
	


	def get_response(self,statement):
		for x in self.Rules:
			if x.does_match_rule(statement):
				response = x.generate_response(statement)
				#Database causing issues, will fix later.
				#self.db.insertQA(statement,response)
				return response



	def create_rules(self):
		self.Rules = []

		# response to "how does that make you feel"
		self.Rules.append( Rule( 'how (does|do) (?P<topic>\w+) make you feel' , "i feel happy about ?topic .", None))

		# response to "im a doctor"
		self.Rules.append( Rule( 'im a doctor', 'no, i\'m the doctor .', None))

		# Ida plays chess.
		#chess_func = lambda instr : os.system('xboard')
		self.Rules.append( Rule( 'do you (know)? (how to)? (play)? chess', "why, yes . i do .", self.cmd_func("xboard")))
		self.Rules.append( Rule( 'do you play chess', "why, yes . i do .", self.cmd_func("xboard")))

		#rule to interpret system exit
		die_func = lambda instr : sys.exit()
		self.Rules.append( Rule( 'die', "goodbye", die_func))

		#perhaps add a rule to go back to a previous repsonse or question
		#must be the last rule
		self.Rules.append( Rule( '^.*' , "you are a moron .", None))



	# Utility function, returns a lambda that accepts a string and makes a command line call to cmd.
	def cmd_func(self, cmd):
		return lambda instr : os.system(cmd + " &")
