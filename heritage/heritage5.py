def f(w):
    if w not in m:
        m[w] = d.get(w, 0) + sum(d.get(l, 0) * f(r) for l, r in ((w[:i], w[i:]) for i in range(1, len(w))))
    return m[w]
N, W = input().split()
d = {w : int(m) for w, m in (input().split() for _ in range(int(N)))}
m = {}
print(f(W) % (10**9+7))
