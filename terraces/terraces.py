from collections import defaultdict

x, y = [int(x) for x in input().split()]
garden = [[int(x) for x in input().split()] for _ in range(y)]

graph = defaultdict(list)
for i in range(y):
	for j in range(x):
		if i != 0:
			graph[(i, j)].append((i-1, j))
		if i != y-1:
			graph[(i, j)].append((i+1, j))
		if j != 0:
			graph[(i, j)].append((i, j-1))
		if j != x-1:
			graph[(i, j)].append((i, j+1))
data = [['u' for _ in range(x)] for _ in range(y)]

for i in range(y):
	for j in range(x):
		if data[i][j] == 'u':
			pools = 1
			chain = set()

			stack = [(i, j)]
			while len(stack) != 0:
				u = stack.pop()
				chain.add(u)
				for v in graph[u]:
					if v not in chain:
						if garden[u[0]][u[1]] == garden[v[0]][v[1]]:
							stack.append(v)
						elif garden[u[0]][u[1]] > garden[v[0]][v[1]]:
							pools = 0

			for a, b in chain:
				data[a][b] = pools

print(sum(x for sublist in data for x in sublist))
