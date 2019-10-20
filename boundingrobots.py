from sys import stdin
for line in stdin:
	if line == '0 0\n':
		break

	w, l = [int(x)-1 for x in line.split()]
	thinks = [0, 0]
	actually = [0, 0]

	for _ in range(int(input())):
		direction, distance = input().split()
		distance = int(distance)
		if direction == 'u':
			thinks[1] += distance
			actually[1] = min(actually[1]+distance, l)
		elif direction == 'd':
			thinks[1] -= distance
			actually[1] = max(actually[1]-distance, 0)
		elif direction == 'l':
			thinks[0] -= distance
			actually[0] = max(actually[0]-distance, 0)
		else:
			thinks[0] += distance
			actually[0] = min(actually[0]+distance, w)

	print('Robot thinks', thinks[0], thinks[1])
	print('Actually at', actually[0], actually[1], '\n')
