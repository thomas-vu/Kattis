def f(x, y):
    if x <= 0 or y <= 0:
        return d
    if (x, y) not in memo:
        memo[(x, y)] = sum(f(x-a, y-b) for a, b in (ab[i:i+2] for i in range(0, len(ab), 2))) + c
    return memo[(x, y)]

for _ in range(int(input())):
    *ab, c, d = [int(x) for x in input().split()]
    xy = [int(x) for x in input().split()]
    memo = {}
    for x, y in (xy[i:i+2] for i in range(0, len(xy), 2)):
        print(f(x, y))
    print()
