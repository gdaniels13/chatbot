import re

class Question:
	def __init__(self,question,dynamic):
		self.question = question
		self.dynamic = dynamic

	def get_question(self,topic=""):
		if self.dynamic:
			t = self.question.split();
			for i in range(len(t)):
				if t[i][0] == '?':
					t[i] = topic
			return ' '.join(t)
		else:
			return self.question

