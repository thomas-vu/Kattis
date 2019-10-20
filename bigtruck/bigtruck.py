from collections import defaultdict
import heapq

n = int(input())
items = {i : int(x) for i, x in zip(range(1, n+1), input().split())}
graph = defaultdict(list)
for _ in range(int(input())):
	a, b, d = [int(x) for x in input().split()]
	graph[a].append((b, d))
	graph[b].append((a, d))

item = defaultdict(int)
item[1] = items[1]
dist = {i : float('inf') for i in range(1, n+1)}
dist[1] = 0
pq = [(dist[1], 1)]
visited = set()
while pq:
	u = heapq.heappop(pq)[1]
	visited.add(u)
	for v, w in graph[u]:
		if v not in visited:
			if dist[u] + w < dist[v]:
				dist[v] = dist[u] + w
				item[v] = item[u] + items[v]
			elif dist[u] + w == dist[v] and item[v] < item[u] + items[v]:
				item[v] = item[u] + items[v]
			heapq.heappush(pq, (w, v))

print(str(dist[n]) + ' ' + str(item[n]) if dist[n] != float('inf') else 'impossible')
