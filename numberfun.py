for _ in range(int(input())):
	a, b, c = [int(x) for x in input().split()]
	print('Possible' if a+b==c or a-b==c or b-a==c or a*b==c or a/b==c or b/a==c else 'Impossible')
