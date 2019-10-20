l, m = map(int, input().split())
ans = (float('inf'), [])

for _ in range(m):
	n, *pctr = input().split(',')
	p, c, t, r = map(int, pctr)

	if 10080 * c * t / (t + r) >= l:
		if p < ans[0]:
			ans = (p, [n])
		elif p == ans[0]:
			ans[1].append(n)

print('\n'.join(ans[1]) if ans[1] else 'no such mower')
