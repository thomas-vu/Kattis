def solve(word):
    if word not in memo:
        memo[word] = d.get(word, 0) + sum(d.get(left, 0) * solve(right) for left, right in ((word[:i], word[i:]) for i in range(1, len(word))))
    return memo[word]

N, W = input().split()
d = {w : int(m) for w, m in (input().split() for _ in range(int(N)))}
memo = {}
print(solve(W) % (10**9+7))
