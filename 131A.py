#python 2.7

#read chars
chars = raw_input()

#check if we should change the chars
#should change if chars are all capitals or all capitals except the first one

def all_capital(chars):
	'''
	@input:
		chars str
	@output:
		bool
	if chars are all capital, return True else False
	'''
	for c in chars:
		if ord(c) >= 97:
			return False

	return True 

def check(chars):
	'''
	@input:
		chars str
	@output:
		bool
	if chars match the rules, return True else False
	'''
	if all_capital(chars[1:]):
		return True
	else:
		return False

def reverse_char(chars):
	char_list = list(chars)
	for i,c in enumerate(char_list):
		if ord(c) < 97:
			char_list[i] = chr(ord(c)+32)
		else:
			char_list[i] = chr(ord(c)-32)

	return ''.join(char_list) 

#check chars
if check(chars):
	print reverse_char(chars)
else:
	print chars
