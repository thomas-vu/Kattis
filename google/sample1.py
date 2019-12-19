def solution(A):
    rows = []
    for h in A:
        if len(rows) == 0:
            rows.append(h)
        else:
            diff = 1000000
            ind = -1
            for i, x in enumerate(rows):
                if x-h > 0 and x-h < diff:
                    diff = x-h
                    ind = i
            if diff < 1000000:
                rows[ind] = h
            else:
                rows.append(h)
    return len(rows)

A = [int(x) for x in input().split()]
print(solution(A))
