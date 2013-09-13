
from theBrain import Brain



# A small function to strip input down to the first phrase or sentence, to
# remove punctuation and captialization, and to replace superfluous whitespace.
# It returns the input as tokenized, capitalized, puctuation devoid words.
def input_tenderizer(input_str):
    # Begin by tokenizing the sentence into individual, whitespace separated
    # components.
    # temp = input_str.lower()
    temp = input_str.lower().translate(None, ',.?!:;\'\"').split()
    # temp = temp.split()

    # Remove any punctuation from the tokens in temp.
    #for x in temp:
	#    x = x.translate(None, ',.?!:;\'\"').upper()
    # We might be able to terminate the sentence with str.find

    # Return the list.
    return ' '.join(temp)


brain = Brain()
brain.otherPersonName = 'Sigmund'
var = "hello"
print(var)
while (var != "Die"):
    var = raw_input('<' + brain.otherPersonName + '> ')
#	print '<' + brain.name + '> ' + brain.whatNext(input_tenderizer(var))
#	print '<' + brain.name + '> ' + input_tenderizer(var)
    print '<' + brain.name + '> ' + brain.whatNext(input_tenderizer(var)).upper()

print("You killed me....")
