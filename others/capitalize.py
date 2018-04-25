#	Program that accepts sequence of lines as input and prints the lines after
#	capitalizing all the characters

sentences = []
print '''To enter sentence(s) to capitalize "proceed" however if you
don't want to proceed but to see the result press "n"'''
		
x = raw_input("Press enter to continue: ")

while x != "n":
	print "Enter sentence: "
	x = raw_input("> ")
	y = x.upper()
	if x != "n":
		sentences.append(y)

	
print '\n'.join(sentences)
	


