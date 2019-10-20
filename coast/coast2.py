from collections import defaultdict, deque

Y, X = [int(x) for x in raw_input().split()]
soteholm = [[0] * (X+2)]
for _ in range(Y):
	soteholm += [[0] + [int(x) for x in raw_input()] + [0]]
soteholm.append([0] * (X+2))

#for x in soteholm:
	#print(''.join(str(i) for i in x))

graph = defaultdict(list)
for i in range(Y+2):
	for j in range(X+2):
		if i != 0:
			graph[(i, j)].append((i-1, j))
		if i != Y+1:
			graph[(i, j)].append((i+1, j))
		if j != 0:
			graph[(i, j)].append((i, j-1))
		if j != X+1:
			graph[(i, j)].append((i, j+1))
#print(graph)

ans = 0
queue = deque()
queue.append((0, 0))
visited = set()
while queue:
	u = queue.popleft()
	visited.add(u)
	for v in graph[u]:
		if soteholm[v[0]][v[1]] == 1:
			ans += 1
		elif v not in visited:
			queue.append(v)
			visited.add(v)

print ans
