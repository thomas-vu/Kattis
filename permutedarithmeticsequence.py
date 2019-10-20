for _ in range(int(input())):
	n, *m = [int(x) for x in input().split()]

	diff = m[0] - m[1]
	for i in range(n-1):
		if m[i] - m[i+1] != diff:
			break
	else:
		print('arithmetic')
		continue
 
	m.sort()
	diff = m[0] - m[1]
	for i in range(n-1):
		if m[i] - m[i+1] != diff:
			print('non-arithmetic')
			break
	else:
		print('permuted arithmetic')
