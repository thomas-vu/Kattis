s = input()
dp = []
for c in s:
	for i, x in enumerate(dp):
		if c == x:
			break
		if c < x:
			dp[i] = c
			break
	else:
		dp.append(c)
print(26-len(dp))
