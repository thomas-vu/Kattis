import heapq

N, T = [int(x) for x in input().split()]
queue = [[] for _ in range(47)]
for _ in range(N):
    ci, ti = [int(x) for x in input().split()]
    queue[ti].append(ci)

pq = []
ans = 0
for ti in queue[::-1]:
    for ci in ti:
        heapq.heappush(pq, -ci)
    if pq:
        ans -= heapq.heappop(pq)

print(ans)
