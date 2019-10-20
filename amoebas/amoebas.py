from collections import defaultdict

m, n = [int(x) for x in input().split()]
grid = [input() for _ in range(m)]

black = []
for i in range(m):
	for j in range(n):
		if grid[i][j] == '#':
			black.append((i, j))

graph = defaultdict(list)
for i in range(m):
	for j in range(n):
		if i != 0 and j != 0:
			graph[(i, j)].append((i-1, j-1))
		if i != 0:
			graph[(i, j)].append((i-1, j))
		if i != 0 and j != n-1:
			graph[(i, j)].append((i-1, j+1))
		if j != 0:
			graph[(i, j)].append((i, j-1))
		if j != n-1:
			graph[(i, j)].append((i, j+1))
		if i != m-1 and j != 0:
			graph[(i, j)].append((i+1, j-1))
		if i != m-1:
			graph[(i, j)].append((i+1, j))
		if i != m-1 and j != n-1:
			graph[(i, j)].append((i+1, j+1))

ans = 0
while black:
	ans += 1
	stack = [black.pop()]
	visited = set(stack)
	while stack:
		for v in graph[stack.pop()]:
			if grid[v[0]][v[1]] == '#' and v not in visited:
				black.remove(v)
				stack.append(v)
				visited.add(v)

print(ans)
