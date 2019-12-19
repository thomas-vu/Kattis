from sys import stdin
from collections import deque
import heapq

for line in stdin:
    status = [True, True, True]
    stack = []
    queue = deque()
    pq = []
    cardinality = 0
    for _ in range(int(line)):
        op, val = [int(x) for x in input().split()]
        if op == 1:
            cardinality += 1
            stack.append(val)
            queue.append(val)
            heapq.heappush(pq, -val)
        else:
            if cardinality == 0:
                status = [False, False, False]
            else:
                cardinality -= 1
                if stack.pop() != val:
                    status[0] = 0
                if queue.popleft() != val:
                    status[1] = 0
                if heapq.heappop(pq) != -val:
                    status[2] = 0

    if sum(status) == 0:
        print('impossible')
    elif sum(status) > 1:
        print('not sure')
    elif status[0]:
        print('stack')
    elif status[1]:
        print('queue')
    elif status[2]:
        print('priority queue')
