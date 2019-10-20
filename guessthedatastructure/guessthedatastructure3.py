from sys import stdin
from collections import deque
import heapq

for line in stdin:
	is_stack = is_queue = is_pq = 1
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
				is_stack = is_queue = is_pq = 0
			else:
				cardinality -= 1
				if stack.pop() != val:
					is_stack = 0
				if queue.popleft() != val:
					is_queue = 0
				if heapq.heappop(pq) != -val:
					is_pq = 0

	if is_stack + is_queue + is_pq == 0:
		print('impossible')
	elif is_stack + is_queue + is_pq > 1:
		print('not sure')
	elif is_stack:
		print('stack')
	elif is_queue:
		print('queue')
	elif is_pq:
		print('priority queue')
