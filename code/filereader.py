from __future__ import with_statement

class My_File:
	def __init__(self, file_name):
		self.wordList = []
		with open(file_name) as f:
			for line in f:
				self.wordList.append(line.rstrip())
		self.wordList.sort()

	def getList(self):
		return self.wordList