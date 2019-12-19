T, N = [int(x) for x in input().split()]
breaks = [int(x) for x in input().split()] 

dp = [[T if i < breaks[0] else i-breaks[0] for i in range(T+1)]]

for i, x in enumerate(breaks[1:]):
    row = [T for _ in range(T+1)]
    for j in range(breaks[0], T+1):
        row[j] = min(dp[i][j-x], dp[i][j])
    dp.append(row)

sol = []
col = T
for i in range(N-1, 0, -1):
    if dp[i][col] != dp[i-1][col]:
        sol.append(1)
        col -= breaks[i]
    else:
        sol.append(2)
sol.append(1)

onesum = 0
twosum = 0
ans = []

for b, x in zip(sol[::-1], breaks):
    if b == 1:
        ans.append(str(onesum))
        onesum += x
    else:
        ans.append(str(twosum))
        twosum += x

print(' '.join(ans))
