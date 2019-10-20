from collections import defaultdict

m, n = [int(x) for x in input().split()]
graph = defaultdict(list)
for _ in range(m):
	a, b = input().split()
	graph[a].append(b)

for _ in range(n):
	w1, w2 = input().split()
	match = True
	if len(w1) != len(w2):
		match = False
	else:
		for c1, c2 in zip(w1, w2):
			if c1 != c2:
				visited = set()
				stack = [c1]
				while stack:
					u = stack.pop()
					if u == c2:
						break
					for v in graph[u]:
						if v not in visited:
							visited.add(v)
							stack.append(v)
				else:
					match = False
		
	print('yes' if match else 'no')
