n, m = [int(x) for x in input().split()]

d = {}
for _ in range(n):
    x, y = input().split(' -> ')
    d[x] = y
    
old = input()
for _ in range(m):
    new = ''
    for c in old:
        new += d.get(c, c)
    old = new
print(old)
