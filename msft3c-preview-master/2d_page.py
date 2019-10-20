def solve(C, L, X):
    if not (1 <= C <= L):
        return 'ERR'
    result = ['1']

    page = 1
    # result.append('1')
    page += 1

    if page < C - X:
        result.append('...')
        page = C - X

    while page <= min(C + X, L):
        result.append(str(page))
        page += 1

    if page < L:
        result.append('...')
        result.append(str(L))

    return ' '.join(result)

while True:
    try:
        print(solve(*map(int, raw_input().split(','))))
    except:
        break
