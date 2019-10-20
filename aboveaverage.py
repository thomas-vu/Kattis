for _ in range(int(input())):
	N, *grades = [int(x) for x in input().split()]
	avg = sum(grades) / N
	pct = '%0.3f' % (sum(1 for x in grades if x > avg)/N*100)
	print(pct + '%')
