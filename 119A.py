#python 2.7

#gcd

def gcd(x,y):
	if y == 0:
		return x
	if x < y:
		return gcd(y,x)
	else:
		return gcd(y, x-y)

#improved gcd

def igcd(x,y):
	if y == 0:
		return x
	if x < y:
		return gcd(y,x)
	else:
		if x&1 == 0 and y&1 == 0:
			return 2*gcd(x>>1, y>>1)
		if x&1 == 0:
			return gcd(x>>1, y)
		if y&1 == 0:
			return gcd(x, y>>1)
		return gcd(y, x-y)

a_num, b_num, stone_num = raw_input().split()

id = 0
num = [int(a_num), int(b_num)]
stone_num = int(stone_num)

while 1:
	taken_num = igcd(num[id],stone_num)
	if taken_num > stone_num:
		break
	stone_num -= taken_num
	id += 1
	id %= 2

#winner id
id += 1
id %= 2

print id