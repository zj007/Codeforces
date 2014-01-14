#!/usr/bin/python

num = int(raw_input())

l = range(num)

for i, e in enumerate(raw_input().split()):
	l[int(e) - 1] = i + 1

print ' '.join([str(e) for e in l])


