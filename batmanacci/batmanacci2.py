N, K = [int(x) for x in input().split()]
if N == 1:
	print('N')
elif N == 2:
	print('A')
else:
	a = 'N'
	b = 'A'
	for _ in range(N-2):
		a, b = b, a+b
		print(b)
	print(b[K-1])
