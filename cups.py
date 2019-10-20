D = {}

for _ in range(int(input())):
	a, b = input().split()
	try:
		color = a
		radius = int(b)
	except:
		color = b
		radius = int(a) / 2
	D[radius] = color

for k in sorted(D):
	print(D[k])

#############################

D = {}

for _ in range(int(input())):
	a, b = input().split()
	try:
		D[int(b)] = a
	except:
		D[int(a) / 2] = b

for k in sorted(D):
	print(D[k])
