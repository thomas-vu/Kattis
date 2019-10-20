from math import radians, sin, cos
for _ in range(int(input())):
	v0, theta, x1, h1, h2 = [float(x) for x in input().split()]
	t = x1 / (v0 * cos(radians(theta)))
	yt = v0 * t * sin(radians(theta)) - 0.5 * 9.81 * t**2
	print('Safe' if h1+1 <= yt <= h2-1 else 'Not Safe')
