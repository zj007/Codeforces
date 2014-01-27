#!/usr/bin/python
#python 2.7
#Codeforces 263A
#author<Jun Zhao>

row = -1
adjust_steps = 0
for i in xrange(5):
	row += 1
	try:
		position = raw_input().split().index('1')
		#print position
	except:
		continue
	else:
		adjust_steps =  abs(position - 2) + abs(row - 2)

print adjust_steps

