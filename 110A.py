
num_str = raw_input()
lucky_num = num_str.count('7') + num_str.count('4')
if lucky_num == 4 or lucky_num == 7:
	print 'YES'
else:
	print 'NO'
	