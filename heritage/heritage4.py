from collections import defaultdict

def solve(word):
    if word not in memo:
        sol = d[word]
        for left, right in ((word[:i], word[i:]) for i in range(1, len(word))):
            sol += d[left] * solve(right)
        memo[word] = sol
    return memo[word]

N, W = input().split()
d = defaultdict(int)
for w, m in (input().split() for _ in range(int(N))):
    d[w] = int(m)
memo = {}
print(solve(W) % (10**9+7))
