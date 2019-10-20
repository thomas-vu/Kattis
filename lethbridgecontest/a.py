n, h, m = [int(x) for x in input().split()]
minn = h
maxx = h
for _ in range(m):
	h += int(input())
	if h < minn:
		minn = h
	if h > maxx:
		maxx = h

ans = ('.' * (minn-1)) + ('Z' * (maxx-minn+1)) + ('.' * (n-maxx))
print(ans[:h-1] + 'B' + ans[h:])
