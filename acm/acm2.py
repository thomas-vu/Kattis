penalty = {}
solved = 0
total = 0
line = input()
while line != '-1':
	time, problem, result = line.split()
	if result == 'wrong':
		if problem in penalty:
			penalty[problem] += 20
		else:
			penalty[problem] = 20
	else:
		solved += 1
		if problem in penalty:
			total += int(time) + penalty[problem]
		else:
			total += int(time)
	line = input()
print(solved, total)
