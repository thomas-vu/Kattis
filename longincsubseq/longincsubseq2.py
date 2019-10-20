try:
	while True:
		n = int(input())
		s = [int(x) for x in input().split()]
		dp = []
		for c in s:
			for i, x in enumerate(dp):
				if c == x[-1]:
					break
				if c < x[-1]:
					dp[i][-1] = c
					break
			else:
				dp.append(dp[-1] + [c] if dp else [c])
		print(len(dp[-1]))
		print(' '.join(str(s.index(x)) for x in dp[-1]))
except:
	pass
