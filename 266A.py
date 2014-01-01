#python 2.7

raw_input()

remove_num = 0
colors = raw_input()
front_color = 'C'
for c in colors:
	if c == front_color:
		remove_num += 1
	else:
		front_color = c

print remove_num
