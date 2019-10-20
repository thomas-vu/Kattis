from collections import defaultdict, deque

items = [input() for _ in range(int(input()))]
coloring = defaultdict(int)
graph = defaultdict(list)
for _ in range(int(input())):
	u, v = input().split()
	graph[u].append(v)
	graph[v].append(u)

while items:
	source = items.pop()
	coloring[source] = 1
	queue = deque([source])
	while queue:
		u = queue.popleft()
		ucolor = coloring[u]
		for v in graph[u]:
			if coloring[v] == ucolor:
				print('impossible')
				raise SystemExit
			elif coloring[v] == 0:
				coloring[v] = 2 if ucolor == 1 else 1
				queue.append(v)
				items.remove(v)

print(' '.join(key for key in coloring if coloring[key] == 1))
print(' '.join(key for key in coloring if coloring[key] == 2))
