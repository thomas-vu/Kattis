QALY = 0
for _ in range(int(input())):
    q, y = [float(x) for x in input().split()]
    QALY += q * y
print(QALY)
