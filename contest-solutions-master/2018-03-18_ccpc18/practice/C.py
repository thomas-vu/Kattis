def solve(a, b, c):
    return a * b == c or a == b * c or b == a * c or a + b == c or a - b == c or b - a == c

for _ in range(int(input())):
    print('Possible' if solve(*map(int, input().split())) else 'Impossible')