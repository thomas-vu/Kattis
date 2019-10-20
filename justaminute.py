ans = 0
m = 0
for _ in range(int(input())):
	M, S = [int(x) for x in input().split()]
	ans += S/60
	m += M
print(ans/m if ans/m > 1 else 'measurement error')
