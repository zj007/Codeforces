#!/usr/bin/python
#python 2.7
#Codeforces 268A
#author<Jun Zhao>

home = []
guest = []
cnt = 0
for i in xrange(int(raw_input())):
	h, g = raw_input().split()
	home.append(h)
	guest.append(g)


for h in home:
	cnt += guest.count(h)

print cnt