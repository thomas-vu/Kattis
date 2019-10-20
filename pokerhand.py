from collections import defaultdict
d = defaultdict(int)
for c in input().split():
	d[c[0]] += 1
print(max(d.values()))
