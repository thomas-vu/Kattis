def adj(rc):
    r, c = rc[0], rc[1]
    for a, b in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        if 0 <= r+a < R and 0 <= c+b < C:
            yield r+a, c+b

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
