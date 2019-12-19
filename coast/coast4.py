from collections import defaultdict

n, m = [int(x) for x in raw_input().split()]
soteholm = ['0' * (m+2)] + ['0' + raw_input() + '0' for _ in range(n)] + ['0' * (m+2)]

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

ans = 0
stack = [(0, 0)]
visited = set(stack)
while stack:
    for v in graph[stack.pop()]:
        if soteholm[v[0]][v[1]] == '1':
            ans += 1
        elif v not in visited:
            stack.append(v)
            visited.add(v)

print ans
