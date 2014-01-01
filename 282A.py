#python 2.7

x = 0
for i in xrange(int(raw_input())):
	if '++' in raw_input():
		x += 1
	else:
		x -= 1

print x