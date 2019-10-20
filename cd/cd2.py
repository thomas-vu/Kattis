line = input()
while line != '0 0':
	N, M = [int(x) for x in line.split()]
	jack = set(input() for _ in range(N))
	jill = set(input() for _ in range(M))
	print(len(jack & jill))
	line = input()
