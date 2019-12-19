for _ in range(int(input())):
    P, R, F = [int(x) for x in input().split()]
    year = 0
    while P <= F:
        year += 1
        P *= R
    print(year)
