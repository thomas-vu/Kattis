from sys import stdin
for _ in stdin:
    codomain = input().count(' ')
    A = set()
    B = set()
    n = int(input())
    for _ in range(n):
        a, _, b = input().split()
        #a, b = input().split()[::2]
        #a, b = input().split(' -> ')
        A.add(a)
        B.add(b)
    if len(A) < n:
        print('not a function')
    elif len(B) == n == codomain:
        print('bijective')
    elif len(B) == n:
        print('injective')
    elif len(B) == codomain:
        print('surjective')
    else:
        print('neither injective nor surjective')
