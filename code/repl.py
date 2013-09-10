
from theBrain import Brain

brain = Brain()
brain.otherPersonName = 'george'
var = "hello"
print(var)
while (var != "Die"):
	var = raw_input('<' + brain.otherPersonName + '>')
	print '<' + brain.name + '> ' + brain.whatNext(var)

print("You killed me....")