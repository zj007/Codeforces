

c1 = int(raw_input())
c2 = int(raw_input())
c3 = int(raw_input())
c4 = int(raw_input())
count = int(raw_input())


def igcd(x,y):
	if y == 0:
		return x
	if x < y:
		return igcd(y,x)
	else:
		if x&1 == 0 and y&1 == 0:
			return 2*igcd(x>>1, y>>1)
		if x&1 == 0:
			return igcd(x>>1, y)
		if y&1 == 0:
			return igcd(x, y>>1)
		return igcd(y, x-y)


def lcm(x,y):
	return x*y/igcd(x,y)



N1 = [c1, c2, c3, c4]
N2 = [lcm(c1,c2), lcm(c1,c3), lcm(c1,c4),
      lcm(c2,c3), lcm(c2,c4), lcm(c3,c4)]
N3 = [lcm(N2[0],c3), lcm(N2[0],c4), lcm(N2[1],c4), lcm(N2[3],c4)]
N4 = [lcm(N3[0],c4)]



N1 = sum([count/e for e in N1])
N2 = sum([count/e for e in N2])
N3 = sum([count/e for e in N3])
N4 = sum([count/e for e in N4])



print N1 - N2 + N3 - N4

