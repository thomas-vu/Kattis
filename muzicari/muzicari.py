T, N = [int(x) for x in input().split()]
breaks = [int(x) for x in input().split()] 

old = {0 : ''}

for x in breaks:
    new = {}
    for k in old:
        if k+x not in new:
            new[k+x] = old[k] + '1'
        if k-x not in new:
            new[k-x] = old[k] + '2'
    old = new

lowestdiff = 1000000
for x in new:
    if x >= 0 and x < lowestdiff:
        lowestdiff = x

print(new[lowestdiff])

onesum = 0
twosum = 0
ans = []

for b, x in zip(new[lowestdiff], breaks):
    if b == '1':
        ans.append(str(onesum))
        onesum += x
    else:
        ans.append(str(twosum))
        twosum += x

print(onesum)
print(twosum)
print(' '.join(ans))
