N, T, K = map(int, input().split())
C = [0] * T
for c in map(int, input().split()):
	C[c-1] += 1

has = sum(1 for c in C if c == 2)

A = []
for i in range(T):
	buy, sell = map(int, input().split())
	buy *= 2 - C[i]
	sell *= C[i]
	A.append((buy + sell, buy, sell))
A.sort()

profit = 0
for i in range(T):
	if i < K:
		profit -= A[i][1]
	else:
		profit += A[i][2]
print(profit)