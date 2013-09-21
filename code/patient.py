import sys
import os
import re
from database import Database
from rule import Rule
from filereader import My_File
from question import Question
from random import choice
from random import shuffle
from madfibs import MadFibs

class Patient:
	def __init__(self,name='Ida',dbName='memory.sqlite'):
		self.name=name
		self.db = Database(dbName)
		self.create_rules()
		self.Questions = []
		self.create_questions()
		self.response_index = 0
		self.response_modulo = 3
		self.possible_topics = []
		self.recent_topics = []
		self.file = My_File('nouns')
		self.possible_topics = self.file.get_nouns()
		shuffle(self.Questions)
		shuffle(self.Rules)

	def refresh(self,rule,pattern):
		self.recent_topics = [];
		self.create_rules()
		self.create_questions()
		self.possible_topics = self.file.get_nouns()
		shuffle(self.Questions)
		shuffle(self.Rules)


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
		found_rule=False
		response=""
		self.parse_topic(statement)
		for x in self.Rules:
			if x.does_match_rule(statement):
				response = x.generate_response(statement)
				found_rule = True
				break	

				
		#only ask a question if we dont know what to say
		if not found_rule:
			response += self.get_question()
		return response

	def parse_topic(self,input):
		for x in input.split():
			if x in self.possible_topics != -1:
				self.recent_topics.append(x)

	def get_topic(self):
		if len(self.recent_topics) > 0:
			return choice(self.recent_topics)
		else:
			return choice(self.possible_topics)


	def get_story(self,bob,george):
		print '<'+self.name+'> '+ MadFibs().generate_narrative()


	def create_rules(self):
		self.Rules = []

		# response to "how does that make you feel"
		self.Rules.append( Rule( ['how (does|do) (?P<topic>.+) make you feel'] , ["i feel happy about ?topic .","i feel happy about destroying ?topic .", "i hate ?topic ."], None))

		# response to "im a doctor"
		self.Rules.append( Rule( ['im a doctor'], ['no, i\'m the doctor', 'thats nice','what makes you so smart'], None))


		self.Rules.append( Rule( ['what is wrong'], ['everything','nothing','something'], None))

		# Ida plays chess.
		self.Rules.append( Rule( ['do you play chess'], ["why, yes . i do ."], None))

		#rule to interpret system exit
		die_func = lambda instr, bob : sys.exit()
		self.Rules.append( Rule( ['die'], ["goodbye"], die_func))

##maybe put your thing here about the short story.

		self.Rules.append( Rule( ['tell me more'], [' '], self.get_story))
		self.Rules.append( Rule( ['why do you feel that way'], ['my dog died', 'i got a job','i need help'], None))
		self.Rules.append( Rule( ['how are you'], ['im upset','im happy'], None))
		self.Rules.append( Rule( ['do you like computer programming'], ['no, do you', 'yes why do you ask'], None))
		self.Rules.append( Rule( ['why do you always wear those sunglasses'], ['i dont want to be here'], None))
		self.Rules.append( Rule( ['what is your favorite color'], ['purple, what is yours'], None))
		self.Rules.append( Rule( ['what is your name','whats your name'], [self.name + " what is yours"], None))
		self.Rules.append( Rule( ['how does playing checkers make you feel'], ['it doesnt, i like chess, lets play....that was fun'], self.cmd_func("xboard")))
		self.Rules.append( Rule( ['how did you illness make you feel'], ['i dont get sick'], None))
		self.Rules.append( Rule( ['are you beautiful'], ['sometimes','my mommy said i was special','perhaps','what do you think'], None))
		self.Rules.append( Rule( ['where are you family'], ['chicago','utah','mars','they live in the interwebs','san francisco'], None))
		self.Rules.append( Rule( ['where did you live before you came here'], ['heaven'], None))
		self.Rules.append( Rule( ['what happened','where have you been'], ['i got sick', 'my dog died', 'my dad died'], None))
		self.Rules.append( Rule( ['call me (?P<topic>.+)','my name is (?P<topic>.+)'],['ok ill call you ?topic'], self.set_other_name))
		self.Rules.append( Rule( ['pys'],['here is what i am thinking'],self.print_state))
		self.Rules.append( Rule( ['rys'],['im all fresh'],self.refresh))

		self.Rules = self.Rules + self.read_rules_from_file()

		#perhaps add a rule to go back to a previous repsonse or question
		#must be the last rule
		#self.Rules.append( Rule( ['^.*'] , ["lets talk about ."], None))

	def read_rules_from_file(self):
		t = My_File("patterns").get_patterns()
		t = t+My_File("ppatterns").get_patterns()
		return t



	# Utility function, returns a lambda that accepts a string and makes a command line call to cmd.
	def cmd_func(self, cmd):
		return lambda instr : os.system(cmd + " &")



	def get_question(self):
		return choice(self.Questions).get_question(self.get_topic())



	def create_questions(self):
		t=My_File("questions").get_questions()
		t = t + My_File("pquestions").get_questions()
		self.Questions = t
		