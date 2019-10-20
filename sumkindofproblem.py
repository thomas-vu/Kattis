for _ in range(int(input())):
	K, N = [int(x) for x in input().split()]
	S1 = (N+1) * N // 2
	S2 = N * N
	S3 = N * N + N
	print(K, S1, S2, S3)
