"""In cryptography, a Caesar cipher is a very simple encryption
techniques in which each letter in the plain text is replaced
by a letter some fixed number of positions down the alphabet.
For example, with a shift of 3, A would be replaced by D, B would
become E, and so on. The method is named after Julius Caesar, who
used it to communicate with his generals. ROT-13 ("rotate by 13 places")
is a widely used example of a Caesar cipher where the shift is 13.
In Python, the key for ROT-13 may be represented by means of the
following dictionary:

key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z',
       'n':'a', 'o':'b', 'p':'c', 'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h',
       'v':'i', 'w':'j', 'x':'k', 'y':'l', 'z':'m',

       'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 'G':'T', 'H':'U',
       'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z',
       'N':'A', 'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H',
       'V':'I', 'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}
Your task in this exercise is to implement an encoder/decoder of
ROT-13. Once you're done, you will be able to read the following
secret message:

   Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!
Note that since English has 26 characters, your ROT-13 program
will be able to both encode and decode texts written in English."""

from string import ascii_letters, ascii_lowercase, ascii_uppercase, punctuation, digits, whitespace

alpha = 13
key_base = {}

def key_encode():
	if ascii_lowercase:
		for c in list(ascii_lowercase):
			if (ord(c)+13) <= ord(list(ascii_lowercase)[-1]):
				key_base[c] = chr(ord(c)+13)
			else:
				key_base[c] = chr(ord(c)-13)
	if ascii_uppercase:
		for c in list(ascii_uppercase):
			if (ord(c)+13) <= ord(list(ascii_uppercase)[-1]):
				key_base[c] = chr(ord(c)+13)
			else:
				key_base[c] = chr(ord(c)-13)
	if punctuation:
		for c in list(punctuation):
			key_base[c] = chr(ord(c))
	if digits:
		for c in list(digits):
			key_base[c] = c
	if  whitespace:
		key_base[' '] = ' '

	return key_base


def caesar_cypher(text):
	key_base = key_encode()
	cipher_text = ''
	for c in text:
		cipher_text += key_base[c]
	print('{:*^30}'.format('Caesar cipher'))
	print('Original Text: '+text)
	print('Ciphered Text: '+cipher_text)
	print('\n')



caesar_cypher('Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!')
caesar_cypher('This is funny! 99')
