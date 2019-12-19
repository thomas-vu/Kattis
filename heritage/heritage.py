from collections import defaultdict

# f('mark') = [('mark'), ('m', 'ark'), ('ma', 'rk'), ..., ('m', 'a', 'r', 'k')]
def f(word):
    ret = []
    for i in range(2 ** (len(word)-1)):
        new = ''
        for ch, dot in zip(word, format(i, '0' + str(len(word)-1) + 'b')):
            new += ch + (' ' if dot == '1' else '')
        new += word[-1]
        ret.append(new)
    for i, x in enumerate(ret):
        ret[i] = x.split()
    return ret

def solve(word):
    if len(word) == 1:
        return d[word] if word in d else 0

    if word in memo:
        return memo[word]

    sol = d[word] if word in d else 0
    uh = f(word)[1:]
    print(uh)
    for construction in uh:
        prod = 1
        for substring in construction:
            prod *= solve(substring)
        sol += prod
        print(word, sol)
    memo[word] = sol
    return sol

N, W = input().split()
d = {w : int(m) for w, m in (input().split() for _ in range(int(N)))}

memo = {}

#s = set()
#for construction in f(W):
#    for substring in construction:
#        s.add(substring)
#print('\n'.join(sorted(s, key=len)))

print(solve(W))
print(memo)

# m ark
# ma rk
# mar k

# h eimark
# he imark
# hei mark
# heim ark
# heima rk
# heimar k
