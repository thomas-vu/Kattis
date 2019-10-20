def batmanacci(n):
	if n == 1:
		return 'N'
	if n == 2:
		return 'A'
	if n not in memo:
		memo[n] = batmanacci(n-2) + batmanacci(n-1)
	return memo[n]

N, K = [int(x) for x in input().split()]
memo = {}
print(batmanacci(N)[K-1])
