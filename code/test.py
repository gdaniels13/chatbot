from filereader import My_File

t = My_File("questions")

for x in t.get_questions():
	print x.question

