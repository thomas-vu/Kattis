import heapq
A, B, T, a, b = map(int, input().split())
C = int(input())
C = sorted(tuple(map(int, input().split())) for _ in range(C))

best = 0
cur = 0
h = []
for x, y in C:
	cost1 = max(x - A, 0) * a
	heapq.heappush(h, -y)
	cur += 1
	while h and cost1 + max(-h[0] - B, 0) * b > T:
		heapq.heappop(h)
		cur -= 1
	best = max(best, cur)
print(best)