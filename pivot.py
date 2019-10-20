input()
A = [int(x) for x in input().split()]

high = 0
a = set()
for x in A:
	if x > high:
		a.add(x)
		high = x

low = float('inf')
b = set()
for x in A[::-1]:
	if x <= low:
		b.add(x)
		low = x

print(len(a & b))
