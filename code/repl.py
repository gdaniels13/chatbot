from patient import Patient



# A small function to strip input down to the first phrase or sentence, to
# remove punctuation and captialization, and to replace superfluous whitespace.
# It returns the input as tokenized, capitalized, puctuation devoid words.
def input_tenderizer(input_str):
    # Begin by tokenizing the sentence into individual, whitespace separated
    # components.
    temp = input_str.lower().translate(None, ',.?!:;\'\"').split()

    # Remove any punctuation from the tokens in temp.
    #for x in temp:
	#    x = x.translate(None, ',.?!:;\'\"').upper()
    # We might be able to terminate the sentence with str.find

    # Return the list.
    return ' '.join(temp)


patient = Patient()
patient.otherPersonName = 'individual'
#var = "Hello, cruel world!"
#print(var)
#while (var != "Die"):

print "Hello " + patient.otherPersonName
while True:
    print '<' + patient.name + '> ' + patient.get_response(input_tenderizer(raw_input('<' + patient.otherPersonName + '> '))).lower().capitalize();

print("Goodbye, cruel world!")
