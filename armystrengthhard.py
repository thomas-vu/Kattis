for _ in range(int(input())):
	input()
	input()
	G = max(int(x) for x in input().split())
	M = max(int(x) for x in input().split())
	print('Godzilla' if G >= M else 'MechaGodzilla')
