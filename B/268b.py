#!/usr/bin/python
#author<Jun Zhao>

#in  out
#1   1     f(1) = 1
#2   3     f(2) = 2 + 1
#3   7     f(3) = 3 + (3-2)*(2-1) + f(2)
#4   14    f(4) = 4 + (4-3)*((3-1) + (2-1)) + f(3)
#f(n)  = n + (n-2 + ... + 1) + f(n-1) = f(n-1) + (n-2)*(n-1)/2 + n
#f(1) = 1 f(2) = 
#f(n) = ((n-2)*(n-1) + (n-3)*(n-2) + ... + 0*1)/2 + (n + n-1 + ... + 2) + f(1)
#	  = 

def tryTimes1(buttonNums):
	if buttonNums == 1:
		return 1
	return tryTimes(buttonNums - 1) + \
	(buttonNums - 2)*(buttonNums -1)/2 + buttonNums

def tryTimes2(buttonNums):
	t = 1
	for i in range(2,buttonNums+1):
		t = t + (i - 2)*(i - 1)/2 + i
	return t


print tryTimes2(int(raw_input()))
