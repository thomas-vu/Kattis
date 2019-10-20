N, K = [int(x) for x in input().split()]
gallery = [(int(l), int(r)) for l, r in (input().split() for _ in range(N))]

old = [(gallery[0][0], gallery[0][1])]

for row in range(1, N):
    new = []
    for k in range(row + 1):
        if k == 0:
            prev = min(old[k][0], old[k][1])
            left = min(gallery[row][0], prev)
            right = min(gallery[row][1], prev)
        elif k == row:
            left = gallery[row][0] + old[k-1][0]
            right = gallery[row][1] + old[k-1][1]
        else:
            prev = min(old[k][0], old[k][1])
            left = min(gallery[row][0] + old[k-1][0], prev)
            right = min(gallery[row][1] + old[k-1][1], prev)
        new.append((left, right))
    old = new

if K == 0:
    print(sum(x for sublist in gallery for x in sublist))
else:
    print(sum(x for sublist in gallery for x in sublist) - min(new[K-1][0], new[K-1][1]))
