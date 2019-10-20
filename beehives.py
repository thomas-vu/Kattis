import math

line = input().split()
while line[0] != '0.0':
	d, N = float(line[0]), int(line[1])

	sour = 0
	hives = []

	for _ in range(N):
		x, y = [float(x) for x in input().split()]
		hives.append((x,y))

	for i, hive in enumerate(hives):
		for j, hive2 in enumerate(hives):
			if i != j and math.sqrt((hive[0]-hive2[0])**2 + (hive[1]-hive2[1])**2) < d:
				sour += 1
				break
				
	print(sour, 'sour,', N-sour, 'sweet')
	line = input().split()
