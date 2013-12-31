#python 2.7

#read the amount of problems
problems_num = int(raw_input())
problems_solved_num = 0

for i in xrange(problems_num):
	solution_ability = raw_input().split()
	if sum([int(s_a) for s_a in solution_ability]) >= 2:
		problems_solved_num += 1

print problems_solved_num

