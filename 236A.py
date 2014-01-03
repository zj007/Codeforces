
name = raw_input()
distinct_num = len(set(name))

if distinct_num & 1 == 1:
	print 'IGNORE HIM!'
else:
	print 'CHAT WITH HER!'
