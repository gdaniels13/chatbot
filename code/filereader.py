from __future__ import with_statement

class My_File:
	def __init__(self, file_name):
		with open(file_name) as f:
			for line in f:
				print line