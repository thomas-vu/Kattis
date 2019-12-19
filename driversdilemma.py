c, x, m = [float(x) for x in input().split()]
table = [(float(mph), float(mpg)) for mph, mpg in (input().split() for _ in range(6))]

for mph, mpg in table[::-1]:
    gph = (mph / mpg) + x # try without brackets
    hours = m / mph
    if gph*hours < c/2:
        print('YES', int(mph))
        exit()

print('NO')

# try distance >= m
