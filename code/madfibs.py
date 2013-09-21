import string
import random



# Utility class for generating insults of varying intensity.
class Insult:

	# Idea, give the class a list of acceptable profane elements.
	def __init__(self):
		self.obscene = False
		self.rot13 = string.maketrans(
			"ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz",
			"NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")



	# Allow enable or disable rot13 decoding of obscene phrases.
	def set_obscene(obscene):
		self.obscene = obscene



	# This solution is sort of inelegant, ill have to fix it later.
	# If no obscenity argument is given, the default obcenity setting is used.
	def get_insult(self, level, obscene=None):
	
		# Insults are encoded in rot13 as to render the source code inoffensive.
		if obscene==None:
			obscene = self.obscene

		insult=""

		# Level 0 is "stealth" insult mode.
		if level == 0:
				insult = "I refuse to have a battle of wits with an unarmed person."
		elif level == 1:
			insult = "Your mother was a hampster, and your father smelt of elderberries!"
		elif level == 2:
			insult = "Get thee to a Nunnery!"
		elif level == 3:
			insult = "Piss off."
		elif level == 4:
			insult = "Son of a @!#$%."
		elif level == 5:
			insult = "Go die in !@#$ you !@#$%^-^%$#@!*&^ after choking on your own @#$! you son of a @!$#%^* @#^%$!!!!"
		else:
			insult = "Not cool, man."

			return string.translate(insult, rot13)

##change noting abce me





class MadFibs:

	def __init__(self):
		self.insult = Insult()
		self.emotions = ['happy','sad','angry','suicidal','moody','tired','pastoral','calm']
		self.verbs = ['eating','playing','running','exploding','killing','destroying','stabbing','shooting','throwing']
		self.nouns = ['puppy','cat','pet','chair','parent','chainsaw','store','book','house','black bear','toy']


	def generate_narrative(self):

		# Frankly, Ida is not in the mood for storytelling if her mood level is below 10 (very angered).
		# if mood < 10:
		#	 return self.insult.get_insult(3)

	   	narrative = ""
		

		# Generate an introduction to the narrative.
		narrative += self.get_intro()

		# Generate a variable length narrative body.
		narrative += self.get_body()
		narrative += self.get_body()
		

		# Generate a conclusion.
		narrative += self.get_end()


			# Substitute choices from the topiclist into the narrative. Return result.
		return self.insert_topics(narrative)



	def insert_topics(self, narrative):

		# Analyze the string for topics, pick consistent entries and then substitute the choices in.
		response_list = narrative.split()
		for i,x in enumerate(response_list):
			if (x[0] == '?'):
				response_list[i] = self.get_word_type(x.split('?')[1])
		return ' '.join(response_list)


	def get_intro(self):
		return random.choice(["Once upon a time, i was feeling ?emotion because ?noun was ?verb me .",
							"A long time ago, i was involved in uber- ?verb .",
							"When i was a child, i had a ?noun ."])

	def get_body(self):
		return random.choice(["Then my ?noun , was ?verb .",
							"Then I was ?verb with my friend, which made me feel ?emotion about life .",
							"That made me feel ?emotion and ?emotion while my ?noun was ?verb a ?noun ."])


	def get_end(self):
		return random.choice(["And that's how i learned to stop worrying and love the ?noun .",
								"What do you think doc .",
								"So what do you think .",
								"In other words, yo momma's fat ."])

	def get_word_type(self, wordtype):
		wordtype=wordtype.rstrip().lstrip()
		if wordtype =='verb':
			return random.choice(self.verbs)
		elif wordtype =='emotion':
			return random.choice(self.emotions)
		elif wordtype =='noun':
			return random.choice(self.nouns)
		else:
			return "pie"

