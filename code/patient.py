import sys
import os
import re
from database import Database
from rule import Rule
from filereader import My_File
from question import Question
from random import choice


class Patient:
	def __init__(self,name='Ida',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
		self.create_rules()
		self.create_questions()

		self.response_index = 0
		self.response_modulo = 3
		self.possible_topics = []
		self.recent_topics = []
		
		file = My_File('nouns')
		self.possible_topics = file.wordList

	def print_state(self, rule, pattern):
		print self.recent_topics
		print self.response_index
		 

	def set_name(self,name):
		self.name=name
	
	def set_other_name(self,rule,name):
		t = re.match(rule.pattern_str, name)
		self.otherPersonName = t.group(1)

	def get_response(self,statement):
		self.response_index += 1


		response=""
		self.parse_topic(statement)
		for x in self.Rules:
			if x.does_match_rule(statement):
				response = x.generate_response(statement)
				break	

				
		#only ask a question if we dont know what to say
		if response =="":
			response += self.get_question()

		return response

	def parse_topic(self,input):
		for x in input.split():
			if x in self.possible_topics != -1:
				self.recent_topics.append(x)

	def get_topic(self):
		if len(self.recent_topics) > 0:
			return self.recent_topics.pop()
		else:
			return choice(self.possible_topics)


	def create_rules(self):
		self.Rules = []

		# response to "how does that make you feel"
		self.Rules.append( Rule( ['how (does|do) (?P<topic>\w+) make you feel'] , ["i feel happy about ?topic .","i feel happy about destroying ?topic .", "i hate ?topic ."], None))

		# response to "im a doctor"
		self.Rules.append( Rule( ['im a doctor'], ['no, i\'m the doctor', 'thats nice'], None))


		self.Rules.append( Rule( ['what is wrong'], ['everything','nothing','something'], None))

		# Ida plays chess.
		self.Rules.append( Rule( ['do you play chess'], ["why, yes . i do ."], self.cmd_func("xboard")))

		#rule to interpret system exit
		die_func = lambda instr : sys.exit()
		self.Rules.append( Rule( ['die'], ["goodbye"], die_func))

		self.Rules.append( Rule( ['tell me more'], [''], None))
		self.Rules.append( Rule( ['why do you feel that way'], ['my dog died', 'i got a job','i need help'], None))
		self.Rules.append( Rule( ['how are you'], ['im upset','im happy'], None))
		self.Rules.append( Rule( ['do you like computer programming'], ['no, do you', 'yes why do you ask'], None))
		self.Rules.append( Rule( ['why do you always wear those sunglasses'], ['i dont want to be here'], None))
		self.Rules.append( Rule( ['what is your favorite color'], ['purple, what is yours'], None))
		self.Rules.append( Rule( ['what is your name'], [self.name + " what is yours"], None))
		self.Rules.append( Rule( ['how does playing checkers make you feel'], ['it doesnt, i like chess, lets play....that was fun'], self.cmd_func("xboard")))
		self.Rules.append( Rule( ['how did you illness make you feel'], ['i dont get sick'], None))
		self.Rules.append( Rule( ['are you beautiful'], [''], None))
		self.Rules.append( Rule( ['where are you family'], [''], None))
		self.Rules.append( Rule( ['where did you live before you came here'], ['heaven'], None))
		self.Rules.append( Rule( ['what happened'], ['i got sick', 'my dog died', 'my dad died'], None))
		self.Rules.append( Rule( ['call me (?P<topic>\w+)','my name is (?P<topic>\w+)'],['ok ill call you ?topic'], self.set_other_name))
		self.Rules.append( Rule(['pys'],['here is what i am thinking'],self.print_state))

		#perhaps add a rule to go back to a previous repsonse or question
		#must be the last rule
		#self.Rules.append( Rule( ['^.*'] , ["lets talk about ."], None))


	# Utility function, returns a lambda that accepts a string and makes a command line call to cmd.
	def cmd_func(self, cmd):
		return lambda instr : os.system(cmd + " &")



	def get_question(self):
		return choice(self.Questions).get_question(self.get_topic())



	def create_questions(self):
		self.Questions = []
		self.Questions.append(Question("How does that make you feel?",False))
		self.Questions.append(Question('why did you ask me about ?',True))
		self.Questions.append(Question('is ? your favorite',True))
		self.Questions.append(Question('do you like ?',True))
		self.Questions.append(Question('do you have a family',True))
		self.Questions.append(Question('have you ever destroyed a ?',True))
		self.Questions.append(Question('have you ever made a ?',True))
		self.Questions.append(Question('do you own a ?',True))
