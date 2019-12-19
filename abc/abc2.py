d = {k: v for k, v in zip('ABC', sorted(map(int, input().split())))}
print(' '.join(str(d[c]) for c in input()))

d = dict(zip('ABC', sorted(map(int, input().split()))))
print(' '.join(str(d[c]) for c in input()))

d = dict(zip('ABC', sorted(int(x) for x in input().split())))
print(' '.join(str(d[c]) for c in input()))
