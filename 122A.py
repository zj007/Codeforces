#!/usr/bin/python
#python2.7
#Codeforces
#author<Jun Zhao>

number = int(raw_input())

def isLuckyNumber(num):
	if set(str(num)) - set(['4','7']):
		return False
	else:
		return True

#bruteforce
def divisibleByLuckyNumber(num):
	for i in range(4,num/2 + 1):
		if isLuckyNumber(i) and num % i == 0:
			return True
	return False

#judge whether the digit only contains 4 and 7
if isLuckyNumber(number):
	print 'YES'
elif divisibleByLuckyNumber(number):
	print 'YES'
else:
	print 'NO'