import sys; from collections import defaultdict
sys.setrecursionlimit(2000)

def solve(v, steps, universe, ans):
	if steps in ans[v]: return

	ans[v] |= set([steps])
	for child in universe[v]:
		solve(child, steps+1, universe, ans)

#-----------------------------------------------------------------

num_v1, num_v2, num_e1, num_e2 = [int(x) for x in input().split()]
universe1, universe2 = defaultdict(set), defaultdict(set)
ans1, ans2 = defaultdict(set), defaultdict(set)

for i in range(num_e1 + num_e2):
    u, v = [int(x) for x in input().split()]
    if i < num_e1:
        universe1[u].add(v)
    else:
        universe2[u].add(v)

solve(1, 0, universe1, ans1)
solve(1, 0, universe2, ans2)

for _ in range(int(input())):
	q = int(input())
	for x in ans1[num_v1]:
		if q-x in ans2[num_v2]:
			print('Yes')
			break
	else:
		print('No')
