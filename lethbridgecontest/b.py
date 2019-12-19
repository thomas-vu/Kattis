import sys
sys.setrecursionlimit(2000)

n, k = [int(x) for x in input().split()]
hours = []
prices = []
for _ in range(k):
    a, b = [int(x) for x in input().split()]
    hours.append(a)
    prices.append(b)

memo = {}

def solve(n):
    if n <= 0:
        return 0
    if n not in memo:
        ans = float('inf')
        for h, p in zip(hours, prices):
            ans = min(ans, p + solve(n-h))
        memo[n] = ans
    return memo[n]

print(solve(n))
