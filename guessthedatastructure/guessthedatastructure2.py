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
                status[0] = False
                status[1] = False
                status[2] = False
            else:
                cardinality -= 1
                if stack.pop() != val:
                    status[0] = False
                if queue.popleft() != val:
                    status[1] = False
                if heapq.heappop(pq) != -val:
                    status[2] = False

    if status.count(True) == 0:
        print('impossible')
    elif status.count(True) > 1:
        print('not sure')
    elif status[0]:
        print('stack')
    elif status[1]:
        print('queue')
    elif status[2]:
        print('priority queue')
