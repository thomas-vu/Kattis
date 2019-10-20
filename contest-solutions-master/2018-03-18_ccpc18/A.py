a, b = map(int, input().split())
m, s = map(int, input().split())
if a >= b:
	print(a*(m-1) + b)
else:
	x = s - m
	if x < 1:
		x = 1
	print(a * x + b * (m - x))