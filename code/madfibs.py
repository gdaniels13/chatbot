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
        else
	    insult = "Not cool, man."

        return string.translate(insult, rot13)



class MadFibs:

    def __init__(self):
	self.insult = Insult()



    def generate_narrative(self, topiclist, mood):

	# Frankly, Ida is not in the mood for storytelling if her mood level is below 10 (very angered).
	if mood < 10:
	    return self.insult.get_insult(3)

    	narrative = ""
	
	# Generate an introduction to the narrative.
	narrative += get_intro(mood)

	# Generate a variable length narrative body.
	narrative += get_body(mood)
	

	# Generate a conclusion.
	narrative += get_end(mood)


        # Substitute choices from the topiclist into the narrative. Return result.
	return insert_topics(narrative, topiclist, mood)



    def insert_topics(self, narrative, topics, mood):

	# Analyze the string for topics, pick consistent entries and then substitute the choices in.
	response_list = self.pick_next_string().split()

    	for i,x in enumerate(response_list):
    		if x[0] == '?':
    			response_list[i] = t.group(x.split("?")[1])

        return ' '.join(response_list)





    def get_intro(self, mood):
	return "One apon a time."



    def get_body(self, mood):
	return "My dog died."



    def get_end(self, mood):
	return "And then they all died. The End."



    def get_word_type(self, topiclist, wordtype):
	return "bannana"
