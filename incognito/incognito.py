from collections import defaultdict
import itertools

def product(arr):
    p = 1
    for i in arr:
        p *= i
    return p

for _ in range(int(input())):
    att = defaultdict(int)
    for _ in range(int(input())):
        att[input().split()[-1]] += 1

    stuff = [v for v in att.values()]
    ans = 0
    for L in range(1, len(stuff)+1):
        for subset in itertools.combinations(stuff, L):
            print(subset)
            ans += product(subset)

    print(ans)
