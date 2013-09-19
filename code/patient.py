import sys
import os
from database import Database
from rule import Rule


class Patient:
	def __init__(self,name='Ida',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
		self.create_rules()
		self.create_questions()

		self.response_index = 0
		self.response_modulo = 3
		self.recent_topics = []
		self.recent_topic_count = 5
	


	def set_name(self,name):
		self.name=name
	


	def get_response(self,statement):
		self.response_index += 1

		response=""

		for x in self.Rules:
			if x.does_match_rule(statement):
				response = x.generate_response(statement)

				#Database causing issues, will fix later.
				#self.db.insertQA(statement,response)
				if self.response_index%self.response_modulo == 0:
					response += " " + self.get_question()
				break
		return response

	def add_topic(self,newTopic):
		self.recent_topics.append(newTopic)
		if len(self.recent_topics)==self.recent_topic_count:
			self.recent_topics.pop(0)
		print newTopic

	def parse_topic(self,input):
		ignore_list = 
		print input


	def create_rules(self):
		self.Rules = []

		# response to "how does that make you feel"
		self.Rules.append( Rule( 'how (does|do) (?P<topic>\w+) make you feel' , ["i feel happy about ?topic .","i feel happy about destroying ?topic .", "i hate ?topic ."], None))

		# response to "im a doctor"
		self.Rules.append( Rule( 'im a doctor', ['no, i\'m the doctor', 'thats nice'], None))


		self.Rules.append( Rule( 'what is wrong', ['everything','nothing','something'], None))

		# Ida plays chess.
		self.Rules.append( Rule( 'do you play chess', ["why, yes . i do ."], self.cmd_func("xboard")))

		#rule to interpret system exit
		die_func = lambda instr : sys.exit()
		self.Rules.append( Rule( 'die', ["goodbye"], die_func))

		self.Rules.append( Rule( 'tell me more', [''], None))
		self.Rules.append( Rule( 'why do you feel that way', ['my dog died', 'i got a job','i need help'], None))
		self.Rules.append( Rule( 'how are you', ['im upset','im happy'], None))
		self.Rules.append( Rule( 'do you like computer programming', ['no, do you', 'yes why do you ask'], None))
		self.Rules.append( Rule( 'why do you always wear those sunglasses', ['i dont want to be here'], None))
		self.Rules.append( Rule( 'what is your favorite color', ['purple, what is yours'], self.parse_topic))
		self.Rules.append( Rule( 'what is your name', [self.name + "what is yours"], None))
		self.Rules.append( Rule( 'how does playing checkers make you feel', ['it doesnt, i like chess, lets play....that was fun'], self.cmd_func("xboard")))
		self.Rules.append( Rule( 'how did you illness make you feel', ['i dont get sick'], None))
		self.Rules.append( Rule( 'are you beautiful', [''], None))
		self.Rules.append( Rule( 'where are you family', [''], None))
		self.Rules.append( Rule( 'where did you live before you came here', ['heaven'], None))
		self.Rules.append( Rule( 'what happened', [''], None))



		#perhaps add a rule to go back to a previous repsonse or question
		#must be the last rule
		self.Rules.append( Rule( '^.*' , ["you are a moron ."], None))


	# Utility function, returns a lambda that accepts a string and makes a command line call to cmd.
	def cmd_func(self, cmd):
		return lambda instr : os.system(cmd + " &")



	def get_question(self):
		var = self.Questions.pop(0)
		self.Questions.append(var)
		return var



	def create_questions(self):
		self.Questions = []

		self.Questions.append("How does that make you feel?")