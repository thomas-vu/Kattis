# ceiling
how many 3 to be least 10 or ceiling(10/3)
(10 + 3 - 1) // 3 == 4

# unweighted graph
from collections import defaultdict
graph = defaultdict(list)
for _ in range(NUM_EDGES):
    u, v = [int(x) for x in input().split()]
    graph[u].append(v)
    graph[v].append(u) # undirected graph

# weighted graph
from collections import defaultdict
graph = defaultdict(list)
for _ in range(NUM_EDGES):
    u, v, w = [int(x) for x in input().split()]
    graph[u].append((v, w))
    graph[v].append((u, w)) # undirected graph

# dfs
stack = [SOURCE]
visited = set(stack)
while stack:
    for v in graph[stack.pop()]:
        if v not in visited:
            stack.append(v)
            visited.add(v)

# bfs
from collections import deque
queue = deque([SOURCE])
visited = set(queue)
while queue:
    for v in graph[queue.popleft()]:
        if v not in visited:
            queue.append(v)
            visited.add(v)

# dijkstra
import heapq
dist = [float('inf') for _ in range(NUM_NODES)]
dist[SOURCE] = 0
pq = [(dist[SOURCE], SOURCE)]
visited = set()
while pq:
    u = heapq.heappop(pq)[1]    # can I make this consistent
    visited.add(u)                # with bfs/dfs? yes...why? no...why not?
    for v, w in graph[u]:
        if v not in visited:
            dist[v] = min(dist[v], dist[u] + w)
            heapq.heappush(pq, (w, v))
