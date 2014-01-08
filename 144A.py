#!/usr/bin/python
soldiers_num = int(raw_input())

soldiers_height_list = raw_input().split()

def lfind(l, v):
	for i,e in enumerate(l):
		if e == v:
			return i
	return -1

def rfind(l, v):
	for i in reversed(range(len(l))):
		if l[i] == v:
			return i
	return -1




max_height_position = lfind(soldiers_height_list, max(soldiers_height_list))
min_height_position = rfind(soldiers_height_list, min(soldiers_height_list))

if max_height_position < min_height_position or soldiers_num == 1:
	print max_height_position + soldiers_num - 1 - min_height_position
else:
	print max_height_position + soldiers_num - 2 - min_height_position
