d = {k : 0 for k in range(1, 366)}
for _ in range(int(input())):
    si, ti = [int(x) for x in input().split()]
    for i in range(si, ti+1):
        d[i] = 1
print(sum(d.values()))
