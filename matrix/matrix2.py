from sys import stdin
for case, line in enumerate(stdin):
    a, b = [int(x) for x in line.split()]
    c, d = [int(x) for x in input().split()]
    input()
    determinant = a*d-b*c
    print(f'Case {case+1}:')
    print(d//determinant, -b//determinant)
    print(-c//determinant, a//determinant)
