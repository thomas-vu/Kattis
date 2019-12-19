n, x = [int(x) for x in input().split()]
prices = sorted(int(x) for x in input().split())
prev = prices[0]
ans = 1
for p in prices[1:]:
    if prev + p > x:
        break
    prev = p
    ans += 1
print(ans)
