'''
findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect
'''
def findNextSquare(input):
	for i in range(input):
		if i**2 == input:
			nextNum = i+1
			result = nextNum**2
			break
		else:	
			result = -1
	return result

print findNextSquare(164)

# from math import sqrt
# def find_next_square(sq):
#     # Return the next square if sq is a square, -1 otherwise
#     return  (sqrt(sq)+1)*(sqrt(sq)+1) if ((sqrt(sq)+1)*(sqrt(sq)+1)).is_integer() else -1

# print find_next_square(232)
