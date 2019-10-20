from math import sqrt

a, b, c = [int(x) for x in input().split()]
d, e, f = [int(x) for x in input().split()]
g, h, i = [int(x) for x in input().split()]

coords = {a: (0, 0), b: (0, 1), c: (0, 2),
		  d: (1, 0), e: (1, 1), f: (1, 2),
		  g: (2, 0), h: (2, 1), i: (2, 2)}

ans = 0
for i in range(1, 9):
	x1, y1 = coords[i]
	x2, y2 = coords[i+1]
	ans += sqrt((x1-x2)**2 + (y1-y2)**2)
print(ans)
