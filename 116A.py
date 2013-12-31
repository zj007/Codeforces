#python 2.7

#read the amount of stops
stops_num = int(raw_input())

#store the minimum value of capacity
capacity_min = 0

#store the capacity anystop
capacity = 0

#for each stop
for stop in xrange(stops_num):
	out_num,in_num = [int(v) for v in raw_input().split()]
	capacity += in_num - out_num
	if capacity > capacity_min:
		capacity_min = capacity

print capacity_min
