def adj(rc):
	r, c = rc[0], rc[1]
	for a, b in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
	    if 0 <= r+a < R and 0 <= c+b < C:
	        yield r+a, c+b

R, C = [int(x)+2 for x in input().split()]
soteholm = ['0'*C] + ['0'+input()+'0' for _ in range(R-2)] + ['0'*C]

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
