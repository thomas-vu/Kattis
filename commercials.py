n, p = [int(x) for x in input().split()]
viewers = [int(x)-p for x in input().split()]
dp = 0
ans = 0
for x in viewers:
    dp = max(0, dp+x)
    ans = max(ans, dp)
print(ans)
