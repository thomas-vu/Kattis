from collections import defaultdict

while True:
	n = int(input())
	if n == 0: break

	d = defaultdict(list)
	for _ in range(n):
		name, *order = [x for x in input().split()]
		for item in order:
			d[item].append(name)

	for item in sorted(d):
		print(item, ' '.join(name for name in sorted(d[item])))
	print()
