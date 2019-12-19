try:
    case = 1
    while True:
        a, b = [int(x) for x in input().split()]
        c, d = [int(x) for x in input().split()]
        input()
        determinant = a*d-b*c
        print(f'Case {case}:')
        print(d//determinant, -b//determinant)
        print(-c//determinant, a//determinant)
        case += 1
except:
    pass
