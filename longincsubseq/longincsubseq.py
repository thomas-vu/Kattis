try:
	while True:
		n = int(input())
		s = map(int, input().split())
		dp = []
		for j, c in enumerate(s):
			for i, x in enumerate(dp):
				if c == x[-1][0]:
					break
				if c < x[-1][0]:
					dp[i][-1] = (c, j)
					break
			else:
				dp.append(dp[-1] + [(c, j)] if dp else [(c, j)])
		print(len(dp[-1]))
		print(' '.join(str(x[1]) for x in dp[-1]))
except:
	pass
