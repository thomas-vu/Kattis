from collections import defaultdict

n, m = [int(x) for x in input().split()]
grid = ['.' * (m+2)] + [f'.{input()}.' for _ in range(n)] + ['.' * (m+2)]

graph = defaultdict(list)
for i in range(n+2):
    for j in range(m+2):
        if i != 0:
            graph[(i, j)].append((i-1, j))
        if i != n+1:
            graph[(i, j)].append((i+1, j))
        if j != 0:
            graph[(i, j)].append((i, j-1))
        if j != m+1:
            graph[(i, j)].append((i, j+1))

ans = [[0 if grid[i][j] == '.' else '?' for j in range(m+2)] for i in range(n+2)]
level = 0
stack = [(i, j) for i in range(n+2) for j in range(m+2) if grid[i][j] == '.']
visited = set(stack)
while '?' in (x for row in ans for x in row):
    level += 1
    new = []
    while stack:
        for i, j in graph[stack.pop()]:
            if grid[i][j] == 'T' and (i, j) not in visited:
                ans[i][j] = level
                new.append((i, j))
                visited.add((i, j))
    stack = new

pad = 2 if level < 10 else 3
for row in ans[1:-1]:
    print(''.join('.' * (pad-len(str(x))) + (str(x) if x else '.') for x in row[1:-1]))
