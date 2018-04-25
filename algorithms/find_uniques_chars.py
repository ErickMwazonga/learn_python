'''
Write a program that take an input as a sentence then returns the strings that are not repeated.
'''

def find_uniques_chars(str):
	unique_lst = []
	list_str = str.split()

	for s in list_str:
		if list_str.count(s) == 1:
			unique_lst.append(s)

	return unique_lst


print(find_uniques_chars('char the one of a the of'))