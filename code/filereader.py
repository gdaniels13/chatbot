from __future__ import with_statement
from rule import Rule
from question import Question

class My_File:
	def __init__(self, file_name):
		self.file_name=file_name


	def get_nouns(self):
		wordList = []
		with open(self.file_name) as f:
			for line in f:
				wordList.append(line.rstrip())
		return wordList
		
	def get_patterns(self):
		rules = []
		curQuestions = []
		curAnswers = []
		curAction = ""
		f= open(self.file_name,'r')
		line = f.readline().rstrip()
		

		while (line != 'end'):
			line = f.readline().rstrip()
			
			while(line != 'a'):
				curQuestions.append(line)
				line = f.readline().rstrip()
			line = f.readline().rstrip()
			while(line!='q' and line != 'end'):
				curAnswers.append(line)
				line = f.readline().rstrip()
			rules.append( Rule(curQuestions,curAnswers,None))
			curAnswers = []
			curQuestions = []
		return rules

	def get_questions(self):
		questions=[]
		file=open(self.file_name,'r')
		for line in file:
			t = line.rstrip().split('**')
			if t[1] == 'T':
				questions.append(Question(t[0],True))
			else:
				questions.append(Question(t[0],False))
		return questions
