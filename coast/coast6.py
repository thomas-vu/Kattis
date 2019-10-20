def adj(rc):
	r, c = rc[0], rc[1]
	if r-1 >= 0:
		yield r-1, c
	if c-1 >= 0:
		yield r, c-1
	if c+1 < C:
		yield r, c+1
	if r+1 < R:
		yield r+1, c

R, C = [int(x)+2 for x in input().split()]
soteholm = ['0' * C] + [f'0{input()}0' for _ in range(R-2)] + ['0' * C]

ans = 0
stack = [(0, 0)]
visited = set(stack)
while stack:
	for r, c in adj(stack.pop()):
		if soteholm[r][c] == '1':
			ans += 1
		elif (r, c) not in visited:
			stack.append((r, c))
			visited.add((r, c))

print(ans)
