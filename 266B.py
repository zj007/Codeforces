#!/usr/bin/python
_, t = [ int(e) for e in raw_input().split()]
seq = [e for e in raw_input()]

def swap(seq):
	i = 0
	l = len(seq)
	while i < l:
		if i == l- 1:
			break
		if seq[i] == 'B' and seq[i+1] == 'G':
			seq[i] = 'G'
			seq[i+1] = 'B'
			i += 2
		else:
			i += 1





def transform(seq, t):
	for i in xrange(t):
		swap(seq)

transform(seq, t)

print ''.join(seq)

