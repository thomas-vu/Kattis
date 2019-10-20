def adj(rc):
	r, c = rc[0], rc[1]
	for r, c in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1)]:
	    if 0 <= r < R and 0 <= c < C:
	        yield r, c

R, C = [int(x) for x in input().split()]
grid = [input() for _ in range(R)]
black = [(r, c) for r in range(R) for c in range(C) if grid[r][c] == '#']

ans = 0
while black:
	ans += 1
	stack = [black.pop()]
	visited = set(stack)
	while stack:
		for r, c in adj(stack.pop()):
			if (r, c) not in visited and grid[r][c] == '#':
				black.remove((r, c))
				stack.append((r, c))
				visited.add((r, c))

print(ans)
