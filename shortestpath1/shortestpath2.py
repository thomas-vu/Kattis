def main():
    from collections import defaultdict
    import heapq
    
    line = raw_input()
    while line != '0 0 0 0':
        n, m, q, s = [int(x) for x in line.split()]
        graph = defaultdict(list)
        for _ in range(m):
            u, v, w = [int(x) for x in raw_input().split()]
            graph[u].append((v, w))
            #graph[v].append((u, w)) for undirected graphs like the gif
        
        dist = [float('inf') for _ in range(n)]
        dist[s] = 0
        pq = [(dist[s], s)]
        visited = set()
        while pq:
            u = heapq.heappop(pq)[1]
            visited.add(u)
            for v, w in graph[u]:
                if v not in visited:
                    dist[v] = min(dist[v], dist[u] + w)
                    heapq.heappush(pq, (w, v))
    
        for _ in range(q):
            target = int(raw_input())
            print dist[target] if dist[target] != float('inf') else 'impossible'
    
        print
        line = raw_input()

main()
