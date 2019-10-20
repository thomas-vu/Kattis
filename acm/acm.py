from collections import defaultdict
penalty = defaultdict(int)
solved = 0
total = 0
line = input()
while line != '-1':
	time, problem, result = line.split()
	if result == 'wrong':
		penalty[problem] += 20
	else:
		solved += 1
		total += int(time) + penalty[problem]
	line = input()
print(solved, total)
