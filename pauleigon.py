N, P, Q = [int(x) for x in input().split()]
print('paul' if (P+Q)//N % 2 == 0 else 'opponent')
