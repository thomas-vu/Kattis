def adj(rc):
    r, c = rc[0], rc[1]
    if r-1 >= 0 and c-1 >= 0:
        yield r-1, c-1
    if r-1 >= 0:
        yield r-1, c
    if r-1 >= 0 and c+1 < C:
        yield r-1, c+1
    if c-1 >= 0:
        yield r, c-1
    if c+1 < C:
        yield r, c+1
    if r+1 < R and c-1 >= 0:
        yield r+1, c-1
    if r+1 < R:
        yield r+1, c
    if r+1 < R and c+1 < C:
        yield r+1, c+1

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
