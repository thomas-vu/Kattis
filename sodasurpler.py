e, f, c = [int(x) for x in input().split()]
bottles = e + f
drank = 0
while bottles >= c:
    afford = bottles // c
    drank += afford
    bottles -= afford * c
    bottles += afford
print(drank)
