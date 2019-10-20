for _ in range(int(input())):
	input()
	N = int(input())
	if sum(int(input()) for _ in range(N)) % N == 0:
		print('YES')
	else:
		print('NO')
