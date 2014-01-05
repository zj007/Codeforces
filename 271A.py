#!/usr/bin/python

def createNextNum(num):
	num_len = len(num)
	digits = [str(e) for e in range(10)]
	for e in num:
		if e in digits:
			digits.remove(e)
	return num+''.join(digits[:4-num_len])

def findNextNum(curNum):
	for i in [3,2,1,0]:
		for e in range(10)[int(curNum[i])+1:]:
			if len(set(curNum[:i])) == i and str(e) not in curNum[:i]:
				return curNum[:i] + str(e)


print createNextNum(findNextNum(raw_input()))



