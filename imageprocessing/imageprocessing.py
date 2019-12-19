ih, iw, kh, kw = [int(x) for x in input().split()]
image = [[int(x) for x in input().split()] for _ in range(ih)]
kernel = [[int(x) for x in input().split()][::-1] for _ in range(kh)][::-1]

result = [[0 for _ in range(iw-kw+1)] for _ in range(ih-kh+1)]

for i in range(ih-kh+1):
    for j in range(iw-kw+1):
        for y in range(kh):
            for x in range(kw):
                result[i][j] += image[i+y][j+x] * kernel[y][x]

for row in result:
    print(' '.join(str(x) for x in row))
