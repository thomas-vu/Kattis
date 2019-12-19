diag = ['A8', 'B7', 'C6', 'D5', 'E4', 'F3', 'G2', 'H1']
d = {
'B7': ['A6', 'B7', 'C8'],
'C6': ['A4', 'B5', 'C6', 'D7', 'E8'],
'D5': ['A2', 'B3', 'C4', 'D5', 'E6', 'F7', 'G8'],
'E4': ['B1', 'C2', 'D3', 'E4', 'F5', 'G6', 'H7'],
'F3': ['D1', 'E2', 'F3', 'G4', 'H5'],
'G2': ['F1', 'G2', 'H3']
}

for _ in range(int(input())):
    x1, x2, y1, y2 = input().split()
    x = x1 + x2
    y = y1 + y2

    if x == y:
        print('0', x1, x2)

    elif x in diag and y in diag:
        print('1', x1, x2, y1, y2)

    for di in d:
        if x in d[di] and y in d[di]:
            print('1', x1, x2, y1, y2)

    for di in d:
        if x in d[di]:
            for dj in d:
                if y in dj:
                    print('3', x1, x2, di, dj, y1, y2)
