#python 2.7

raw_input()
coin_list = [int(e) for e in raw_input().split()]
coin_list.sort(reverse = True)
total_value = sum(coin_list)
half_value = total_value / 2

mine_value = 0

for i, e in enumerate(coin_list):
	mine_value += e
	if mine_value > half_value:
		break

print i+1


